import re
import pandas as pd
import unicodedata


def clean_text(text: str) -> str:
    """Nettoie le texte en supprimant les accents et la ponctuation."""
    # Normalisation des caractères Unicode
    text = unicodedata.normalize('NFKD', text)
    # Suppression des accents
    text = ''.join([c for c in text if not unicodedata.combining(c)])
    # Conversion en minuscules
    text = text.lower()
    # Remplacement des apostrophes
    text = text.replace("'", " ")
    # Suppression des caractères spéciaux
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # Suppression des espaces multiples
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def label_sentiment(score: int) -> str:
    """Convertit un score numérique en label de sentiment."""
    if score <= 2:
        return "negative"
    elif 3 <= score <= 4:
        return "neutral"
    return "positive"


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Prétraite un dataframe de données textuelles."""
    df = df.copy()
    df['clean_text'] = df['content'].apply(clean_text)
    df['tokens'] = df['clean_text'].apply(lambda x: x.split())
    df['sentiment'] = df['score'].apply(label_sentiment)
    return df