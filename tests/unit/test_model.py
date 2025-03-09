import unittest
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from src.model import load_model_and_tokenizer

class TestModel(unittest.TestCase):
    def test_model_output_shape(self):
        # Charger le modèle et le tokenizer
        tokenizer, model = load_model_and_tokenizer()

        # Créer un exemple de texte
        text = "Ceci est un test."
        inputs = tokenizer(text, return_tensors="pt")

        # Passer à travers le modèle
        outputs = model(**inputs)

        # Vérifier la forme des logits
        self.assertEqual(outputs.logits.shape, torch.Size([1, 2]))  # Supposons que vous avez 2 classes

if __name__ == "__main__":
    unittest.main()