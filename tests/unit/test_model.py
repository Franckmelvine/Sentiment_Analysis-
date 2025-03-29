import unittest
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os


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
        """Configuration avant chaque test."""
        self.model_path = "./results"
        self.tokenizer, self.model = load_model(self.model_path)

    def test_model_loading(self):
        """Vérifie que le modèle et le tokenizer se chargent correctement."""
        self.assertIsNotNone(self.tokenizer, "Le tokenizer n'a pas été chargé correctement.")
        self.assertIsNotNone(self.model, "Le modèle n'a pas été chargé correctement.")

    def test_model_forward_pass(self):
        """Teste un passage avant sur un exemple de texte."""
        sample_text = "C'est une super expérience !"
        inputs = self.tokenizer(sample_text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        self.assertIn("logits", outputs, "Le modèle ne renvoie pas les logits.")

    def test_model_empty_input(self):
        """Test sur une entrée vide pour vérifier la gestion des erreurs."""
        sample_text = ""
        inputs = self.tokenizer(sample_text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        self.assertIn(
            "logits", outputs,
            "Le modèle ne renvoie pas les logits pour une entrée vide."
        )

    def test_model_long_input(self):
        """Test sur une entrée très longue pour vérifier le traitement des textes longs."""
        sample_text = " ".join(["C'est une super expérience !"] * 100)
        inputs = self.tokenizer(
            sample_text, return_tensors="pt", truncation=True, padding=True
        )
        with torch.no_grad():
            outputs = self.model(**inputs)
        self.assertIn(
            "logits", outputs,
            "Le modèle ne renvoie pas les logits pour un texte long."
        )


if __name__ == "__main__":
    unittest.main()
