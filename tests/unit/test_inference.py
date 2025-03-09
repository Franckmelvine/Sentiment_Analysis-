import unittest
from inference import load_model, predict_sentiment

class TestInference(unittest.TestCase):
    def setUp(self):
        self.tokenizer, self.model = load_model()
    
    def test_inference_output(self):
        dummy_text = "Ceci est un avis très positif."
        prediction = predict_sentiment(dummy_text, self.tokenizer, self.model)
        self.assertIsInstance(prediction, int)
        self.assertTrue(0 <= prediction <= 4)  # Vérifier qu'on a bien un label entre 0 et 4

if __name__ == "__main__":
    unittest.main()
