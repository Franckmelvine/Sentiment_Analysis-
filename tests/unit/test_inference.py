import unittest
from src.inference import predict_sentiment  # ✅ Assure-toi que le chemin est correct


class TestInference(unittest.TestCase):
    def setUp(self):
        # ✅ Utilisation d’un modèle public compatible pour éviter l’erreur de config
        self.model_path = "nlptown/bert-base-multilingual-uncased-sentiment"

    def test_prediction_output(self):
        sample_text = "J'adore ce produit, il est génial !"
        result = predict_sentiment(self.model_path, sample_text)

        self.assertIn("label", result)
        self.assertIn("score", result)
        self.assertIsInstance(result["label"], str)
        self.assertIsInstance(result["score"], float)
        self.assertGreaterEqual(result["score"], 0.0)
        self.assertLessEqual(result["score"], 1.0)


if __name__ == "__main__":
    unittest.main()
