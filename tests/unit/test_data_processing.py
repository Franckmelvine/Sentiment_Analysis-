import os
import sys
import unittest
import pandas as pd

# Ajouter 'src' au chemin Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from data_processing import (
    clean_text,
    remove_stopwords,
    lemmatize_text,
    encode_text,
    label_sentiment,
    preprocess_data,
)


class TestDataPreprocessing(unittest.TestCase):

    def test_clean_text(self):
        text = "Hello, World! 123"
        result = clean_text(text)
        self.assertEqual(result, "hello world 123")

    def test_remove_stopwords(self):
        text = "This is a test sentence."
        result = remove_stopwords(text)
        self.assertEqual(result, "test sentence.")

    def test_lemmatize_text(self):
        text = "running better"
        result = lemmatize_text(text)
        self.assertEqual(result, "running better")  # à ajuster selon le vrai comportement

    def test_encode_text(self):
        text = "hello"
        result = encode_text(text)
        self.assertIn("input_ids", result)
        self.assertIn("attention_mask", result)

    def test_label_sentiment(self):
        self.assertEqual(label_sentiment(1), "negative")
        self.assertEqual(label_sentiment(3), "neutral")
        self.assertEqual(label_sentiment(5), "positive")

    def test_preprocess_data(self):
        df = pd.DataFrame({
            "content": ["Good app!", "Worst experience ever."],
            "score": [5, 1]
        })
        df = preprocess_data(df)
        self.assertIn("clean_text", df.columns)
        self.assertIn("tokens", df.columns)
        self.assertIn("sentiment", df.columns)
        self.assertEqual(df["sentiment"].tolist(), ["positive", "negative"])


if __name__ == '__main__':
    unittest.main()
