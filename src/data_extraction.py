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

    except pd.errors.ParserError as e:
        raise pd.errors.ParserError(f"Erreur lors de la lecture du fichier : {e}")


if __name__ == "__main__":
    file_path = r"C:\Users\Franck Melvine\Documents\Aivancity\Bachelor 3\Semestre 2\ML_Ops\dataset.csv"
    
    try:
        # Charge les données
        data = load_data(file_path)
        print("Données chargées avec succès :")
        print(data.head())  # Affiche les 5 premières lignes du DataFrame

    except FileNotFoundError as e:
        print(f"Erreur : {e}")
    except pd.errors.EmptyDataError as e:
        print(f"Erreur : {e}")
    except pd.errors.ParserError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")