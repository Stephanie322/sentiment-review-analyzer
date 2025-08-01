#  Sentiment Review Analyzer

##  Analyze Movie Reviews in One Click

A lightweight Flask web app that scrapes IMDb user reviews, analyzes their sentiment using a pre-trained BERT model, and visualizes the results in a clean 1–5 star chart.

---

## 1.  Introduction

**Sentiment Review Analyzer** is an end-to-end mini project that brings together Natural Language Processing (NLP), web scraping, and data visualization.

This project:

* Uses BeautifulSoup to scrape IMDb reviews
* Applies a multilingual BERT model (`nlptown/bert-base-multilingual-uncased-sentiment`) to analyze sentiments
* Plots a visual summary using Matplotlib
* Runs smoothly as a lightweight Flask web app

It’s designed to demonstrate how ML models can be deployed in real-world applications with live data.

---

## 2.  Visual Helper

The following chart is a sample output of sentiment distribution for a given IMDb review page:

>  The app scores each review from 1 (negative) to 5 (positive), then displays the overall distribution.
<img width="600" height="400" alt="sentiment_chart" src="https://github.com/user-attachments/assets/8d6b45d0-b185-45a9-8715-2d071ddca1ca" />

---

## 3.  Installation Instructions

Make sure you have Python 3.8+ installed.

1. Clone this repository:

```bash
git clone https://github.com/your-username/sentiment-review-analyzer.git
cd sentiment-review-analyzer
```
## 4. Install dependencies:

```bash
pip install -r requirements.txt
```
## 5. (Optional) Download necessary tokenizer/model ahead of time:

-from transformers import AutoTokenizer, AutoModelForSequenceClassification

-AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

-AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

## 6.Running the App Locally:

app.py
Once everything is installed, start the Flask server:
Then go to http://127.0.0.1:5000/ in your browser.
Paste the URL of an IMDb reviews page (e.g., a movie review section), and let the app analyze and visualize the sentiment of the reviews.

## 7. 🐞 Found a Bug? :

If you run into any issues or errors, feel free to open an issue.
Suggestions and contributions are always welcome!

## 8. Known Limitations:

**IMDb-specific scraping: The current implementation relies on a specific HTML class used by IMDb to locate reviews. If IMDb updates their HTML structure or class names (which they frequently do), the scraper will break.
**No error handling for invalid URLs yet (future improvement).
**Static model: Sentiment model is fixed to BERT from nlptown; doesn’t support other models out of the box.

## 9. Tech Stack:

**Python (Flask)

**Transformers (Hugging Face)

**BeautifulSoup (Web Scraping)

**Matplotlib (Data Visualization)

**IMDb (target site)


