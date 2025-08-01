# model.py
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load once (slow)
tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

def get_sentiment_score(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    score = torch.argmax(outputs.logits).item() + 1  # 1 to 5 stars
    return score
