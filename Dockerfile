# Utilise une image plus légère avec Python 3.9
FROM python:3.9-slim

# Désactive les statistiques Streamlit et les warnings Python
ENV BROWSER_GATHER_USAGE_STATS=False \
    PYTHONWARNINGS="ignore::FutureWarning" \
    STREAMLIT_SERVER_PORT=8000

WORKDIR /app

# Installation des dépendances système (optimisée)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Installation des dépendances Python en une seule couche (meilleure pratique Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    python -m spacy download fr_core_news_sm && \
    python -m nltk.downloader popular  # Si vous utilisez NLTK

# Copie des fichiers de l'application (en deux étapes pour mieux utiliser le cache Docker)
COPY src/ src/
COPY *.py ./

# Exposition du port et commande de démarrage
EXPOSE 8000
CMD ["streamlit", "run", "src/app.py", "--server.port=8000", "--server.address=0.0.0.0"]