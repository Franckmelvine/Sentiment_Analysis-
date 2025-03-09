import torch
import unittest
from transformers import AutoModelForSequenceClassification, AutoTokenizer

def load_model(model_path='saved_model'):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return tokenizer, model

class TestModel(unittest.TestCase):
    def setUp(self):
        self.tokenizer, self.model = load_model()
    
    def test_model_output_shape(self):
        dummy_text = "Ceci est un test."
        inputs = self.tokenizer(dummy_text, return_tensors='pt', truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        self.assertEqual(logits.shape, (1, 5))  # Vérifier qu'on a bien 5 classes

if __name__ == "__main__":
    unittest.main()
