FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Installation de spaCy et du modèle français
RUN pip install --upgrade pip && \
    pip install spacy==3.8.3 && \
    python -m spacy download fr_core_news_sm 

# Copier explicitement le dossier src
COPY src ./src

# Vérifier que les fichiers sont bien copiés
RUN ls -R /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py"]
