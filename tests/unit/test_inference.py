import unittest
from inference import predict_sentiment


class TestInference(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test."""
        self.model_path = "./results"

    def test_prediction_output(self):
        """Teste si l'inférence retourne un label et un score valides."""
        sample_text = "J'adore ce produit, il est génial !"

        result = predict_sentiment(self.model_path, sample_text)

        self.assertIn("label", result, "Le résultat doit contenir un label.")
        self.assertIn("score", result, "Le résultat doit contenir un score.")
        self.assertIsInstance(result["label"], str, "Le label doit être une chaîne.")
        self.assertIsInstance(result["score"], float, "Le score doit être un nombre flottant.")
        self.assertGreaterEqual(result["score"], 0.0, "Score trop bas.")
        self.assertLessEqual(result["score"], 1.0, "Score trop élevé.")


if __name__ == "__main__":
    unittest.main()
