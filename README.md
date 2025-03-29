# Sentiment Analysis Pipeline
<<<<<<< HEAD
=======

Ce projet implémente un pipeline d'analyse des sentiments en Python. Il prend en entrée un fichier CSV contenant des textes et leurs sentiment, puis applique différentes étapes de traitement et d'inférence.

## Structure du Projet

```
Sentiment-Analysis-Pipeline/
│── src/
│   ├── __init__.py
│   ├── data_extraction.py  # Chargement des données
│   ├── data_processing.py  # Prétraitement des données
│   ├── inference.py        # Prédiction des sentiments
│   ├── model.py            # Modèle d'analyse des sentiments
│── tests/                  # Tests unitaires
│── dataset.csv             # Fichier de données
│── requirements.txt        # Dépendances du projet
│── README.md               # Documentation du projet
│── test.txt                # Fichier de test
│── .gitignore              # Fichiers à ignorer par Git
```

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/sentiment-analysis-pipeline.git
   cd sentiment-analysis-pipeline
   ```

2. Créez et activez un environnement virtuel :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur macOS/Linux
   venv\Scripts\activate     # Sur Windows
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Placez votre fichier CSV (contenant au moins les colonnes `content` et `score`) dans le dossier racine.
2. Exécutez le script d'extraction des données :
   ```bash
   python src/data_extraction.py
   ```
3. Ajoutez d'autres étapes comme le prétraitement et l'inférence selon vos besoins.

## Développement & Contribution

- Assurez-vous que votre code respecte la structure et les bonnes pratiques de Python.
- Ajoutez des tests unitaires dans le dossier `tests/`.
- Proposez vos améliorations via des pull requests.

## Auteur
Franck Melvine et Owen Diel 

>>>>>>> 814322e459e605fbb43a43f362e9785e62f23d5d
