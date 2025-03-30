import re
import pandas as pd
from typing import List


import unicodedata

def clean_text(text: str) -> str:
    """Nettoie le texte en supprimant les accents et la ponctuation"""
    # Normalise les caractères (décompose les accents)
    text = unicodedata.normalize('NFKD', text)
    # Supprime les caractères diacritiques (accents)
    text = ''.join([c for c in text if not unicodedata.combining(c)])
    # Convertit en minuscule
    text = text.lower()
    # Remplace les apostrophes
    text = text.replace("'", " ")
    # Supprime les caractères spéciaux
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # Supprime les espaces multiples
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def label_sentiment(score: int) -> str:
    """Convertit un score numérique en label de sentiment"""
    if score <= 2:
        return "negative"
    elif 3 <= score <= 4:
        return "neutral"
    else:
        return "positive"

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Prétraite un dataframe de données textuelles"""
    df = df.copy()
    df['clean_text'] = df['content'].apply(clean_text)
    df['tokens'] = df['clean_text'].apply(lambda x: x.split())
    df['sentiment'] = df['score'].apply(label_sentiment)
    return df