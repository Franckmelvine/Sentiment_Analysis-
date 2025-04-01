import re
import pandas as pd
import unicodedata


def clean_text(text: str) -> str:
    """Nettoie le texte en supprimant les accents et la ponctuation."""
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = text.replace("'", " ")
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def label_sentiment(score: int) -> str:
    """Convertit un score numérique en label de sentiment."""
    if score <= 2:
        return "negative"
    if 3 <= score <= 4:
        return "neutral"
    return "positive"


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Prétraite un DataFrame contenant du texte et des scores."""
    df = df.copy()
    df["clean_text"] = df["content"].apply(clean_text)
    df["tokens"] = df["clean_text"].apply(lambda x: x.split())
    df["sentiment"] = df["score"].apply(label_sentiment)
    return df
