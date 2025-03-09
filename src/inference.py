import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

def load_model(model_path='./saved_model'):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return tokenizer, model

def predict_sentiment(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    return predicted_class

if __name__ == "__main__":
    tokenizer, model = load_model()
    text = input("Entrez un avis : ")
    sentiment = predict_sentiment(text, tokenizer, model)
    print(f"Sentiment prédit : {sentiment}")
