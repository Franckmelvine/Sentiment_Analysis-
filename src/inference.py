from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


def load_trained_model(model_path):
    """Charge le modèle et le tokenizer entraînés."""
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return tokenizer, model

def predict_sentiment(model_path, text):
    """Prédit le sentiment d'un texte donné."""
    tokenizer, model = load_trained_model(model_path)
    # Créer un pipeline de classification de texte
    classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)
    result = classifier(text)[0]
    return result

if __name__ == "__main__":
    model_path = "results\logs"  # Modifier selon l'emplacement du modèle sauvegardé
    text = "J'adore cette expérience, c'est incroyable !"  # Exemple de texte
    prediction = predict_sentiment(model_path, text)
    print(f"Texte: {text}\nPrédiction: {prediction['label']} (Score: {prediction['score']:.4f})")
