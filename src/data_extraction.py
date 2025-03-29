import pandas as pd
<<<<<<< HEAD

def load_data(filepath):
    """Charge les données à partir d'un fichier CSV et vérifie les colonnes."""
    try:
        df = pd.read_csv(filepath)
        if "content" not in df.columns or "score" not in df.columns:
            raise ValueError("Le fichier CSV doit contenir les colonnes 'content' et 'score'")
        return df
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
        return None

# Test rapide
if __name__ == "__main__":
    df = load_data(r'C:\Users\moudi\sentiment-analysis-pipeline\dataset.csv')
    if df is not None:
        print(df.head())
=======
import os

def load_data(file_path):
    """
    Charge les données à partir d'un fichier CSV.

    Args:
        file_path (str): Chemin vers le fichier CSV.

    Returns:
        pd.DataFrame: DataFrame contenant les données chargées.

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
        pd.errors.EmptyDataError: Si le fichier est vide.
        pd.errors.ParserError: Si le fichier ne peut pas être analysé.
    """
    # Vérifie si le fichier existe
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier {file_path} n'existe pas.")

    try:
        # Charge les données
        data = pd.read_csv(file_path)

        # Vérifie si le fichier est vide
        if data.empty:
            raise pd.errors.EmptyDataError("Le fichier est vide.")

        return data

    except pd.errors.EmptyDataError as e:
        raise pd.errors.EmptyDataError(f"Le fichier est vide ou ne contient pas de données valides : {e}")

    except pd.errors.ParserError as e:
        raise pd.errors.ParserError(f"Erreur lors de l'analyse du fichier CSV : {e}")

    except Exception as e:
        raise e  # Lève toute autre exception

>>>>>>> 814322e459e605fbb43a43f362e9785e62f23d5d
