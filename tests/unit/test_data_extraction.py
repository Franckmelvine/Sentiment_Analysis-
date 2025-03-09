import sys
import os
import pandas as pd
import unittest

# Ajouter le répertoire parent de 'src' au chemin de recherche de modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from data_extraction import load_data  

class TestDataExtraction(unittest.TestCase):

    def setUp(self):
        """
        Cette méthode est exécutée avant chaque test.
        Elle crée des fichiers temporaires à des fins de test.
        """
        # Création d'un fichier CSV temporaire pour le test
        self.test_file = "test_file.csv"
        with open(self.test_file, 'w') as f:
            f.write("col1,col2\n")
            f.write("data1,data2\n")
            f.write("data3,data4\n")

    def tearDown(self):
        """
        Cette méthode est exécutée après chaque test.
        Elle supprime les fichiers temporaires utilisés pour le test.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_data_success(self):
        """
        Teste la fonction load_data avec un fichier existant.
        """
        data = load_data(self.test_file)
        self.assertIsNotNone(data)  # Vérifie que le retour n'est pas None
        self.assertEqual(len(data), 3)  # Vérifie qu'il y a 3 lignes dans le fichier CSV
        self.assertEqual(list(data.columns), ['col1', 'col2'])  # Vérifie les noms des colonnes

    def test_load_data_file_not_found(self):
        """
        Teste la fonction load_data avec un fichier qui n'existe pas.
        """
        with self.assertRaises(FileNotFoundError):
            load_data("non_existent_file.csv")

    def test_load_data_empty_file(self):
        """
        Teste la fonction load_data avec un fichier vide.
        """
        empty_file = "empty_file.csv"
        with open(empty_file, 'w') as f:
            pass  # Crée un fichier vide

        with self.assertRaises(pd.errors.EmptyDataError):
            load_data(empty_file)

        # Nettoyage
        os.remove(empty_file)

    def test_load_data_invalid_csv(self):
        """
        Teste la fonction load_data avec un fichier CSV invalide.
        """
        invalid_csv = "invalid_file.csv"
        with open(invalid_csv, 'w') as f:
            f.write("invalid data without commas")

        with self.assertRaises(pd.errors.ParserError):
            load_data(invalid_csv)

        # Nettoyage
        os.remove(invalid_csv)

if __name__ == "__main__":
    unittest.main()
