import unittest
from inference import predict_sentiment


class TestInference(unittest.TestCase):
    def setUp(self):
        self.model_path = "./results"

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
