<<<<<<< HEAD
import pytest
import pandas as pd
from src.data_processing import clean_text, preprocess_data, label_sentiment

def test_clean_text():
    assert clean_text("Hello, World!") == "hello world"
    assert clean_text("C'est génial!! 123") == "cest genial 123"

def test_label_sentiment():
    assert label_sentiment(1) == "negative"
    assert label_sentiment(3) == "neutral"
    assert label_sentiment(5) == "positive"

def test_preprocess_data():
    df = pd.DataFrame({"content": ["Good app!", "Worst experience ever."], "score": [5, 1]})
    df = preprocess_data(df)

    assert "clean_text" in df.columns
    assert "tokens" in df.columns
    assert "sentiment" in df.columns
    assert df["sentiment"].tolist() == ["positive", "negative"]
=======
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

import unittest
from data_processing import clean_text, remove_stopwords, lemmatize_text, encode_text  # Changé ici

class TestDataPreprocessing(unittest.TestCase):

    def test_clean_text(self):
        text = "Hello World! 123"
        result = clean_text(text)
        self.assertEqual(result, "hello world")

    def test_remove_stopwords(self):
        text = "This is a test sentence."
        result = remove_stopwords(text)
        self.assertEqual(result, "test sentence.")

    def test_lemmatize_text(self):
        text = "running better"
        result = lemmatize_text(text)
        self.assertEqual(result, "running better")

    def test_encode_text(self):
        text = "hello"
        result = encode_text(text)
        self.assertTrue('input_ids' in result)
        self.assertTrue('attention_mask' in result)

if __name__ == '__main__':
    unittest.main()
>>>>>>> 814322e459e605fbb43a43f362e9785e62f23d5d
