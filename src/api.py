from fastapi import FastAPI
from pydantic import BaseModel
from src.inference import predict_sentiment

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API de détection de sentiments. Allez sur /docs pour tester."}

@app.post("/predict")
def predict(input: TextInput):
    sentiment = predict_sentiment(input.text)
    return {"sentiment": sentiment}
