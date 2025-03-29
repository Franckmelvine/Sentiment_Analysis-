from fastapi import FastAPI
from pydantic import BaseModel
from src.inference import predict_sentiment

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(input: TextInput):
    result = predict_sentiment(input.text)
    return {"sentiment": result[0]['label'], "confidence": result[0]['score']}
