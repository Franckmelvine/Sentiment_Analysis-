from transformers import pipeline

def load_inference_pipeline():
    """Charge le pipeline d'inférence."""
    model_name = "arindamatcalgm/w266_model4_BERT_AutoModelForSequenceClassification"
    return pipeline("text-classification", model=model_name)

def predict_sentiment(pipe, text):
    """Prédit le sentiment d'un texte donné."""
    return pipe(text)

if __name__ == "__main__":
    # Charger le pipeline
    pipe = load_inference_pipeline()

    # Demander à l'utilisateur de saisir un texte
    text = input("Entrez le texte pour l'analyse de sentiment: ")
    result = predict_sentiment(pipe, text)
    print(f"Sentiment: {result[0]['label']}, Confiance: {result[0]['score']:.4f}")