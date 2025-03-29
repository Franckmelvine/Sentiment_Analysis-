# 💬 Sentiment Analysis Pipeline – MLOps Edition

[![Tests](https://github.com/votre-utilisateur/sentiment-analysis-pipeline/actions/workflows/test.yml/badge.svg)]
[![Build](https://github.com/votre-utilisateur/sentiment-analysis-pipeline/actions/workflows/build.yml/badge.svg)]
[![Evaluate](https://github.com/votre-utilisateur/sentiment-analysis-pipeline/actions/workflows/evaluate.yml/badge.svg)]

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
