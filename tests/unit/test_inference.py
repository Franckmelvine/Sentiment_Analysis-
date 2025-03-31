import unittest
from unittest.mock import patch
from src.inference import predict_sentiment


class TestInference(unittest.TestCase):
    @patch("src.inference.predict_sentiment")
    def test_prediction_output(self, mock_predict):
        # On simule la sortie du modèle
        mock_predict.return_value = {
            "label": "positive",
            "score": 0.987
        }

        sample_text = "J'adore ce produit, il est génial !"
        result = predict_sentiment("fake-model-path", sample_text)

        self.assertIn("label", result)
        self.assertIn("score", result)
        self.assertIsInstance(result["label"], str)
        self.assertIsInstance(result["score"], float)
        self.assertGreaterEqual(result["score"], 0.0)
        self.assertLessEqual(result["score"], 1.0)


if __name__ == "__main__":
    unittest.main()
