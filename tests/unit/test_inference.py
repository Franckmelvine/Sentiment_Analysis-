import unittest
from src.inference import load_inference_pipeline, predict_sentiment

class TestInference(unittest.TestCase):
    def test_predict_sentiment(self):
        # Charger le pipeline
        pipe = load_inference_pipeline()

        # Tester un texte
        text = "Ceci est un test positif."
        result = predict_sentiment(pipe, text)

        # Vérifier que le résultat contient un label et un score
        self.assertIn('label', result[0])
        self.assertIn('score', result[0])

if __name__ == "__main__":
    unittest.main()