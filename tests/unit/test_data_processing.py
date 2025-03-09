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