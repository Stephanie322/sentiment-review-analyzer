# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_reviews(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article", class_="sc-a77dbebd-1 iJQoqi user-review-item")

    reviews = []
    for article in articles:
        review_div = article.find("div", {"data-testid": "review-overflow"})
        if review_div:
            reviews.append(review_div.text.strip())

    return reviews
