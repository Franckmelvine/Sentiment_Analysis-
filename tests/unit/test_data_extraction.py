import sys
import os
import pandas as pd
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
from data_extraction import load_data  # noqa: E402


class TestDataExtraction(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_file.csv"
        with open(self.test_file, 'w') as f:
            f.write("col1,col2\n")
            f.write("data1,data2\n")
            f.write("data3,data4\n")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_data_success(self):
        data = load_data(self.test_file)
        self.assertIsNotNone(data)
        self.assertEqual(len(data), 3)
        self.assertEqual(list(data.columns), ['col1', 'col2'])

    def test_load_data_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_data("non_existent_file.csv")
