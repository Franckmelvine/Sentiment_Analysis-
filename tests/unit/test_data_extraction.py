import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
from data_extraction import load_data  # noqa: E402


class TestDataExtraction(unittest.TestCase):
    def test_load_data_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_data("non_existent_file.csv")
