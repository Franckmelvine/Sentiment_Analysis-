import re
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")


def clean_text(text):
    """Nettoie le texte brut en supprimant la ponctuation et les majuscules."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text


def label_sentiment(score):
    """Attribue un label de sentiment selon le score."""
    if score <= 2:
        return "negative"
    elif score == 3:
        return "neutral"
    else:
        return "positive"


def preprocess_data(df):
    """Ajoute des colonnes nettoyées et étiquetées."""
    df["clean_text"] = df["content"].apply(clean_text)
    df["sentiment"] = df["score"].apply(label_sentiment)
    df["tokens"] = df["clean_text"].apply(
        lambda x: tokenizer(x, truncation=True, padding="max_length")
    )
    return df
