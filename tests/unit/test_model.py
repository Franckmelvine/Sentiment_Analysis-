import unittest
import os
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


def load_model(model_path):
    """Charge le modèle et le tokenizer."""
    if not os.path.exists(model_path):
        raise ValueError(
            f"Le chemin spécifié pour le modèle est introuvable : {model_path}"
        )
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return tokenizer, model


class TestModel(unittest.TestCase):
    def setUp(self):
        self.model_path = "./results"
        self.tokenizer, self.model = load_model(self.model_path)

    def test_model_loading(self):
        self.assertIsNotNone(self.tokenizer)
        self.assertIsNotNone(self.model)

    def test_model_forward_pass(self):
        sample_text = "C'est une super expérience !"
        inputs = self.tokenizer(sample_text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        self.assertIn("logits", outputs)

    def test_model_empty_input(self):
        sample_text = ""
        inputs = self.tokenizer(sample_text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        self.assertIn("logits", outputs)

    def test_model_long_input(self):
        sample_text = " ".join(["C'est une super expérience !"] * 100)
        inputs = self.tokenizer(
            sample_text, return_tensors="pt", truncation=True, padding=True
        )
        with torch.no_grad():
            outputs = self.model(**inputs)
        self.assertIn("logits", outputs)


if __name__ == "__main__":
    unittest.main()
