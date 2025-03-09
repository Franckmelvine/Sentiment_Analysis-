import pandas as pd
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

