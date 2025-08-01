from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

# ✅ UPDATED: Real analyzer to scrape + predict
def analyze_reviews(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # You can adjust this selector based on the site you're scraping
    articles = soup.find_all("article", class_="sc-a77dbebd-1 iJQoqi user-review-item")

    reviews = []
    for article in articles:
        review_div = article.find("div", {"data-testid": "review-overflow"})
        if review_div:
            reviews.append(review_div.text.strip())

    data = []
    for review in reviews:
        inputs = tokenizer(review, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits).item() + 1  # Scores: 1 (worst) to 5 (best)
        data.append({"review": review, "sentiment": prediction})

    return pd.DataFrame(data)

# ✅ UPDATED: Handles 1–5 rating scale
def plot_sentiment_chart(df):
    counts = df['sentiment'].value_counts().sort_index()
    labels = ['1⭐', '2⭐', '3⭐', '4⭐', '5⭐']
    counts = counts.reindex([1, 2, 3, 4, 5], fill_value=0)

    plt.figure(figsize=(6,4))
    plt.bar(labels, counts, color='skyblue')
    plt.title('Sentiment Analysis of Reviews')
    plt.ylabel('Number of Reviews')
    plt.xlabel('Sentiment Score')
    plt.tight_layout()

    path = 'static/sentiment_chart.png'
    plt.savefig(path)
    plt.close()
    return path

@app.route("/", methods=["GET", "POST"])
def home():
    chart = None
    if request.method == "POST":
        url = request.form["url"]
        df = analyze_reviews(url)
        chart = plot_sentiment_chart(df)
    return render_template("index.html", chart=chart)

if __name__ == "__main__":
    app.run(debug=True)
