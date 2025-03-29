# 💬 Sentiment Analysis Pipeline – MLOps 

[![Tests](https://github.com/OwenDiel/Sentiment_Analysis-/actions/workflows/test.yml/badge.svg)]
[![Build](https://github.com/OwenDiel/Sentiment_Analysis-/actions/workflows/build.yml/badge.svg)]
[![Evaluate](https://github.com/OwenDiel/Sentiment_Analysis-/actions/workflows/evaluate.yml/badge.svg)]     

---

## 🎯 Objectif

Ce projet vise à déployer un modèle BERT de détection de sentiments dans un pipeline complet de MLOps.  
Il s'agit de la suite directe d’un premier projet où nous avons développé et testé un modèle de classification de sentiments.

---

## 🧱 Structure du projet

```
sentiment-analysis-pipeline/
├── src/
│   ├── data_extraction.py
│   ├── data_processing.py
│   ├── model.py
│   ├── inference.py
│   ├── evaluate.py
│   └── api.py               # API FastAPI
├── tests/
│   └── unit/
│       ├── test_model.py
│       ├── test_inference.py
├── app.py                   # Interface Streamlit
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .github/
│   └── workflows/
│       ├── test.yml
│       ├── evaluate.yml
│       ├── build.yml
│       └── release.yml
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

### 🔧 Build et lancement de l’API

```bash
docker compose up --build
```

📍 L'API est accessible ici : http://localhost:8000/docs

---

## 🔁 Utilisation de l’API FastAPI

```http
POST /predict
Content-Type: application/json

{
  "text": "This is the best app ever!"
}
```

📤 Réponse attendue :

```json
{
  "sentiment": "positive"
}
```

---

## 🧪 Exécution des tests

```bash
pytest
```

> ✅ Tous les tests unitaires sont dans le dossier `tests/unit/`

---

## 🧬 Évaluation automatique du modèle

- Fichier : `src/evaluate.py`
- Génère `metrics.json` contenant l'accuracy
- Le pipeline échoue automatiquement si l'accuracy < 0.75

---

## 🧰 Interface utilisateur (Streamlit)

```bash
streamlit run app.py
```

Interface web simple pour tester rapidement les prédictions de sentiment.

---

## 🛠️ GitHub Actions CI/CD

| Workflow        | Déclencheur                    | Description                                      |
|----------------|--------------------------------|--------------------------------------------------|
| `test.yml`     | push, pull_request             | Exécute les tests unitaires et le linting       |
| `evaluate.yml` | après succès de `test.yml`     | Évalue le modèle et stocke les métriques        |
| `build.yml`    | push sur `main`                | Build l’image Docker                            |
| `release.yml`  | push d’un tag (ex: v1.0.0)      | Crée une release officielle avec changelog      |

---

## 👥 Auteurs & Répartition

| Étudiant      | Tâches principales                          |
|---------------|---------------------------------------------|
| **Melvine**   | Docker, FastAPI, Streamlit, README, Rapport |
| **Owen**      | GitHub Actions, Tests, Évaluation, CI/CD    |

> 🔄 Tous les développements ont été faits en collaboration avec revues de code et pull requests GitHub.

---

## 📄 Rapport de projet

📁 `rapport_MLOps.pdf` : contient :
- L’architecture technique complète
- Les outils utilisés
- Les défis rencontrés et solutions
- Les pistes d’amélioration
- La répartition des rôles

---

## 🔮 Améliorations futures

- Monitoring avec Prometheus + Grafana
- Intégration de MLflow pour le suivi des expériences
- Export CSV des prédictions dans Streamlit
- Déploiement de l’API sur un vrai serveur ou sur le cloud

---

## 🏁 Merci

Projet réalisé dans le cadre du module MLOps  
Mars 2025 – aivancity school for technology business & society



