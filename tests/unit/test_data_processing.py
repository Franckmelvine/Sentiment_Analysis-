import unittest
import pandas as pd
from src.data_processing import clean_text, preprocess_data, label_sentiment


class TestDataProcessing(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text("Hello, World!"), "hello world")
        self.assertEqual(clean_text("C'est génial!! 123"), "c est genial 123")
        self.assertEqual(clean_text("Déjà vu! Ça marche?"), "deja vu ca marche")

    def test_label_sentiment(self):
        self.assertEqual(label_sentiment(1), "negative")
        self.assertEqual(label_sentiment(3), "neutral")
        self.assertEqual(label_sentiment(5), "positive")

    def test_preprocess_data(self):
        test_df = pd.DataFrame({
            "content": ["Excellent!", "Terrible..."],
            "score": [5, 1]
        })
        processed_df = preprocess_data(test_df)

        self.assertEqual(processed_df.shape[0], 2)
        self.assertListEqual(
            processed_df["sentiment"].tolist(),
            ["positive", "negative"]
        )
        self.assertEqual(processed_df["clean_text"].iloc[0], "excellent")


if __name__ == "__main__":
    unittest.main()
