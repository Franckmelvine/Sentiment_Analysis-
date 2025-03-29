from transformers import pipeline

# Charger le modèle UNE SEULE FOIS
pipe = pipeline("text-classification", model="arindamatcalgm/w266_model4_BERT_AutoModelForSequenceClassification")

def predict_sentiment(text):
    """Prédit le sentiment d'un texte donné."""
    return pipe(text)
