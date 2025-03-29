import sys
import os
import unittest
import pandas as pd

# Ajout du chemin du dossier src
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src'))
sys.path.insert(0, base_path)

from data_processing import (  # noqa: E402
    clean_text,
    preprocess_data,
    label_sentiment
)


class TestDataPreprocessing(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text("Hello, World! 123"), "hello world 123")

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
        self.assertIn("sentiment", df_processed.columns)
        expected = ["positive", "negative"]
        self.assertEqual(df_processed["sentiment"].tolist(), expected)


if __name__ == "__main__":
    unittest.main()
