FROM python:3.9-slim

WORKDIR /app

# Installer outils nécessaires
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Mettre à jour pip et installer spaCy + modèle français
RUN pip install --upgrade pip && \
    pip install spacy==3.8.3 && \
    python -m spacy download fr_core_news_sm

# Copier requirements et installer le reste
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet
COPY . .

# Lancer Streamlitv
CMD ["streamlit", "run", "src/app.py", "--server.port=8000", "--server.address=0.0.0.0"]
