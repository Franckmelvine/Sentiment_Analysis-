# 💬 Sentiment Analysis Pipeline – MLOps 

[![Tests](https://github.com/Franckmelvine/Sentiment_Analysis-/actions/workflows/test.yml/badge.svg)](https://github.com/Franckmelvine/Sentiment_Analysis-/actions/workflows/test.yml)
[![Evaluate](https://github.com/Franckmelvine/Sentiment_Analysis-/actions/workflows/evaluate.yml/badge.svg)](https://github.com/Franckmelvine/Sentiment_Analysis-/actions/workflows/evaluate.yml)
[![Build](https://github.com/Franckmelvine/Sentiment_Analysis-/actions/workflows/build.yml/badge.svg)](https://github.com/Franckmelvine/Sentiment_Analysis-/actions/workflows/build.yml)
[![Release](https://github.com/Franckmelvine/Sentiment_Analysis-/actions/workflows/release.yml/badge.svg)](https://github.com/Franckmelvine/Sentiment_Analysis-/actions/workflows/release.yml)   

---

## 🎯 Objectif

Ce projet vise à déployer un modèle BERT de détection de sentiments dans un pipeline complet de MLOps.  
Il s'agit de la suite directe d’un premier projet où nous avons développé et testé un modèle de classification de sentiments.

---

## 🧱 Structure du projet

```
sentiment-analysis-pipeline/
├── .github/
│   └── workflows/
│       ├── test.yml
│       ├── evaluate.yml
│       ├── build.yml
│       └── release.yml
├── src/
│   ├── data_extraction.py
│   ├── data_processing.py
│   ├── model.py
│   ├── inference.py
│   ├── app.py                   # Interface Streamlit
│   ├── api.py                   # API FastAPI
│   ├── evaluate.py
│   └── performance_report.py
├── tests/
│   └── unit/
│       ├── test_model.py
│       ├── test_inference.py
│       ├── test_data_extraction.py
│       ├── test_data_processing.py
├── .flake8
├── .gitignore
├── Dockerfile
├── Dockerfile.api
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation locale

```bash
git clone https://github.com/Franckmelvine/Sentiment_Analysis-.git
cd Sentiment_Analysis-
python -m venv venv
source venv/bin/activate  # sous Windows : venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🐳 Exécution avec Docker

### 🔧 Lancer à la fois l’API FastAPI et l’interface Streamlit :

```bash
docker compose up --build
```

- 📍 Interface utilisateur streamlit: http://localhost:8000
- 📍 Interface APIFast: http://localhost:8001
  ![image](https://github.com/user-attachments/assets/8b58c12b-e077-4eae-898d-eb7fee87bd17)

---

## 🧪 Exécution des tests

```bash
pytest
```

> ✅ Tous les tests unitaires sont dans le dossier `tests/unit/`

---

## 🧬 Évaluation automatique du modèle

- Script : `src/evaluate.py`
- Génère un fichier `metrics.json` contenant l'accuracy
- Le pipeline GitHub échoue si accuracy < 0.75

---

## 🎨 Interface utilisateur (Streamlit)

```bash
streamlit run src/app.py
```
![image](https://github.com/user-attachments/assets/b348b928-8052-48a0-ae59-cae9e5c37ec7)


Permet de tester manuellement le modèle avec retour visuel et coloré.

---

## 🛠️ GitHub Actions CI/CD

| Workflow        | Déclencheur                  | Description                                      |
|----------------|------------------------------|--------------------------------------------------|
| `test.yml`     | push, pull_request           | Exécute linting + tests unitaires               |
| `evaluate.yml` | après succès de `test.yml`   | Évalue les performances et vérifie l’accuracy   |
| `build.yml`    | push sur `main`              | Build et push l’image Docker vers GHCR          |
| `release.yml`  | push d’un tag (ex: v1.0.0)   | Crée automatiquement une release GitHub         |

---

## 📚 Documentation Technique

### 🧠 Architecture MLOps

- **Modèle** : BERT fine-tuné via Hugging Face
- **API** : FastAPI pour servir le modèle
- **Interface utilisateur** : Streamlit
- **Docker** : pour packager API + interface
- **GitHub Actions** : pour tout automatiser via CI/CD

---

### ⚙️ Choix techniques

- 🔹 **Transformers (HuggingFace)** pour le NLP
- 🔹 **FastAPI** pour exposer le modèle en REST
- 🔹 **Docker** pour une portabilité maximale
- 🔹 **GitHub Actions** pour automatiser tests, évaluation, build et release
- 🔹 **.flake8** pour le style de code

---

### 🔄 Flux de travail automatisé

1. Dev push son code sur GitHub
2. `test.yml` est lancé : lint + tests
3. Si succès, `evaluate.yml` est déclenché :
   - évalue les performances
   - échoue si accuracy < 0.75
   - stocke les résultats
4. Si tout est OK, `build.yml` crée et pousse l'image Docker
5. Une release peut être créée via un tag Git (ex: `v1.0.0`)

---

## 📈 Monitoring des performances

### Script automatique : `src/performance_report.py`

Permet d’afficher les résultats de `metrics.json` :

```bash
python src/performance_report.py
```

Exemple de sortie :
```
📊 Rapport de performance :
- Accuracy : 84.20%
```

🔁 Intégré automatiquement dans le workflow `evaluate.yml`.

---

## 👥 Auteurs & Répartition

| Étudiant      | Tâches principales                          |
|---------------|---------------------------------------------|
| **Melvine**   | Docker, FastAPI, Streamlit, README, Rapport |
| **Owen**      | GitHub Actions, Tests, Évaluation, CI/CD    |

> 🔄 Collaboration constante via GitHub : pull requests, revue de code, échanges sur les erreurs

---

## 📄 Rapport de projet

📁 `Rapport_MLOps_Owen_et_Melvine.pdf` : contient :
- L’architecture technique complète
- Les outils utilisés
- Les défis rencontrés et solutions
- Les pistes d’amélioration
- La répartition des rôles

---

## 🔮 Améliorations futures

- Monitoring Prometheus + Grafana
- Tracking des modèles avec MLflow
- Déploiement sur cloud (Railway, Azure, Heroku…)
- Tests d’intégration complets sur l’API

---

## 🏁 Merci

Projet réalisé dans le cadre du module **MLOps**  
📆 Mars 2025 – *aivancity school for technology business & society*
