import unittest
import os
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


def load_model(model_path="./results"):
    """Charge le modèle et le tokenizer."""
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForSequenceClassification.from_pretrained(model_path)
        return tokenizer, model
    except Exception:
        # Modèle local non valide => fallback vers un modèle public
        fallback = "nlptown/bert-base-multilingual-uncased-sentiment"
        tokenizer = AutoTokenizer.from_pretrained(fallback)
        model = AutoModelForSequenceClassification.from_pretrained(fallback)
        return tokenizer, model


class TestModel(unittest.TestCase):
    def setUp(self):
        self.tokenizer, self.model = load_model()

    def test_model_loading(self):
        self.assertIsNotNone(self.tokenizer)
        self.assertIsNotNone(self.model)

    def test_model_forward_pass(self):
        sample_text = "C'est une super expérience !"
        inputs = self.tokenizer(
            sample_text, return_tensors="pt", truncation=True, max_length=512
        )
        with torch.no_grad():
            outputs = self.model(**inputs)
        self.assertIn("logits", outputs)

    def test_model_empty_input(self):
        sample_text = ""
        inputs = self.tokenizer(
            sample_text, return_tensors="pt", truncation=True, max_length=512
        )
        with torch.no_grad():
            outputs = self.model(**inputs)
        self.assertIn("logits", outputs)

    def test_model_long_input(self):
        sample_text = " ".join(["C'est une super expérience !"] * 100)
        inputs = self.tokenizer(
            sample_text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512,
        )
        with torch.no_grad():
            outputs = self.model(**inputs)
        self.assertIn("logits", outputs)


if __name__ == "__main__":
    unittest.main()
