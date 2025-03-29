import pandas as pd
import unittest
from src.data_processing import clean_text, preprocess_data, label_sentiment


class TestDataProcessing(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text("Hello, World!"), "hello world")
        self.assertEqual(clean_text("C'est génial!! 123"), "cest genial 123")

    def test_label_sentiment(self):
        self.assertEqual(label_sentiment(1), "negative")
        self.assertEqual(label_sentiment(3), "neutral")
        self.assertEqual(label_sentiment(5), "positive")

    def test_preprocess_data(self):
        df = pd.DataFrame({
            "content": ["Good app!", "Worst experience ever."],
            "score": [5, 1]
        })
        df_processed = preprocess_data(df)

        self.assertIn("clean_text", df_processed.columns)
        self.assertIn("tokens", df_processed.columns)
        self.assertIn("sentiment", df_processed.columns)
        self.assertEqual(
            df_processed["sentiment"].tolist(), ["positive", "negative"]
        )


if __name__ == "__main__":
    unittest.main()
