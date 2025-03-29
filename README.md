# 💬 Sentiment Analysis Pipeline – MLOps Edition

[![Tests](https://github.com/OwenDiel/sentiment-analysis-pipeline/actions/workflows/test.yml/badge.svg)]
[![Build](https://github.com/OwenDiel/sentiment-analysis-pipeline/actions/workflows/build.yml/badge.svg)]
[![Evaluate](https://github.com/OwenDiel/sentiment-analysis-pipeline/actions/workflows/evaluate.yml/badge.svg)]

## 🚀 Objectif

Ce projet implémente une solution complète de détection de sentiments avec un modèle BERT, intégrée dans un pipeline MLOps avec Docker, GitHub Actions, FastAPI et Streamlit.

---

## 🧱 Structure du Projet

Sentiment-Analysis-Pipeline/
├── .github/
│   └── workflows/
│       ├── test.yml
│       ├── evaluate.yml
│       ├── build.yml
│       └── release.yml
├── src/
│   ├── _init_.py
│   ├── data_extraction.py
│   ├── data_processing.py
│   ├── inference.py
│   ├── model.py
│   └── app.py  # Fichier de déploiement
├── tests/
│   ├── _init_.py
│   ├── test_data.py
│   ├── test_model.py
│   └── test_api.py
├── data/
│   ├── dataset.csv
│   └── test.txt
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore


---

## ⚙️ Installation locale

git clone https://github.com/Franckmelvine/Sentiment_Analysis-.git
cd Sentiment_Analysis-
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
pip install -r requirements.txt 

## 🐳 Utilisation avec Docker
### Lancer l'API avec Docker Compose

docker compose up --build

Puis accéder à la documentation interactive :
📍 http://localhost:8000/docs

## 🧪 Exemple d’appel API

POST /predict
Content-Type: application/json

{
  "text": "This is the best app ever!"
}

### 📤 Réponse attendue :

{
  "sentiment": "positive"
}

## 🧬 Évaluation du modèle
L'évaluation est automatisée via GitHub Actions (evaluate.yml) après chaque test.
Elle génère un fichier metrics.json contenant la précision.

## 🧰 Déploiement Streamlit
Vous pouvez également utiliser l’interface utilisateur via :
streamlit run app.py

Cela ouvre une interface web locale pour soumettre du texte et obtenir des prédictions de sentiment.

## 🛠️ Workflows GitHub Actions

✅ test.yml : exécute les tests unitaires et vérifie le lint

✅ evaluate.yml : évalue le modèle et stocke les métriques

✅ build.yml : build Docker sur main

✅ release.yml : création automatique de release via GitHub tags

## 👥 Auteurs & Répartition
Étudiant	Tâches principales
Melvine	Docker, FastAPI, Streamlit, README, Rapport
Owen	GitHub Actions, tests, évaluation, lint

## 📄 Rapport
Le rapport rapport_MLOps.pdf fournit :

L’architecture technique

Les choix faits

La répartition des tâches

Les problèmes rencontrés et résolus

Des idées d’amélioration future

## 🔮 Améliorations possibles
Intégration de MLflow pour le suivi d’expériences

Ajout de tests d’intégration API

Monitoring avec Prometheus + Grafana

Déploiement via AWS / GCP

## 🏁 Merci !

