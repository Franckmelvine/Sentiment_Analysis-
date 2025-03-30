from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch


def load_trained_model(model_path):
    """Charge le modèle et le tokenizer entraînés."""
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return tokenizer, model


def predict_sentiment(model_path, text):
    """Prédit le sentiment d'un texte donné."""
    tokenizer, model = load_trained_model(model_path)
    classifier = pipeline(
        "text-classification",
        model=model,
        tokenizer=tokenizer,
        device=0 if torch.cuda.is_available() else -1
    )
    result = classifier(text)[0]
    return result


if __name__ == "__main__":
    # ✅ Pour tester localement, utilise un modèle public
    model_path = "nlptown/bert-base-multilingual-uncased-sentiment"
    text = "J'adore cette expérience, c'est incroyable !"
    prediction = predict_sentiment(model_path, text)
    print(
        f"Texte: {text}\nPrédiction: {prediction['label']} "
        f"(Score: {prediction['score']:.4f})"
    )
