# Utiliser une image Python légère
FROM python:3.10-slim

# Créer un répertoire de travail dans le conteneur
WORKDIR /app

# Copier tous les fichiers du projet dans le conteneur
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Démarrer FastAPI avec Uvicorn
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]