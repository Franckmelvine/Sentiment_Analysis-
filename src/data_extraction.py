import pandas as pd


def load_data(file_path):
    """Charge les données depuis un fichier CSV."""
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Fichier introuvable : {file_path}")
    except pd.errors.EmptyDataError:
        raise pd.errors.EmptyDataError(
            f"Le fichier est vide : {file_path}"
        )
    except pd.errors.ParserError:
        raise pd.errors.ParserError(
            f"Erreur de parsing dans le fichier : {file_path}"
        )
