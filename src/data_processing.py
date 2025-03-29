import re
import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s]", "", text)
    return text


def remove_stopwords(text):
    from spacy.lang.fr.stop_words import STOP_WORDS
    return " ".join([word for word in text.split() if word not in STOP_WORDS])


def lemmatize_text(text):
    import spacy
    nlp = spacy.load("fr-core-news-sm")
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc])


def label_sentiment(score):
    if score <= 2:
        return "negative"
    elif score == 3:
        return "neutral"
    else:
        return "positive"


def preprocess_data(df):
    df["clean_text"] = df["content"].apply(clean_text)
    df["no_stopwords"] = df["clean_text"].apply(remove_stopwords)
    df["lemmatized"] = df["no_stopwords"].apply(lemmatize_text)
    df["sentiment"] = df["score"].apply(label_sentiment)
    return df


def encode_text(text, tokenizer=None):
    if tokenizer is None:
        tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    return tokenizer(text, padding="max_length", truncation=True, return_tensors="pt")
