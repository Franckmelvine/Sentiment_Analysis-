import pandas as pd
<<<<<<< HEAD
import re
from transformers import AutoTokenizer
from unidecode import unidecode  # Nouvelle importation

# Charger le tokenizer BERT
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def clean_text(text):
    """Nettoie le texte en supprimant les caractères spéciaux et en mettant en minuscules."""
    text = str(text).lower()
    text = unidecode(text)  # Convertit "génial" en "genial"
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Supprime la ponctuation et caractères spéciaux
    text = re.sub(r"\s+", " ", text).strip()  # Supprime les espaces en trop
    return text

def label_sentiment(score):
    """Convertit les scores en catégories de sentiment."""
    if score <= 2:
        return "negative"
    elif score == 3:
        return "neutral"
    else:
        return "positive"

def preprocess_data(df):
    """Applique le nettoyage et la tokenisation des textes."""
    # Vérifier si les colonnes existent
    if "content" not in df.columns or "score" not in df.columns:
        print(f"Colonnes disponibles : {df.columns}")
        raise KeyError("Les colonnes 'content' et 'score' sont absentes du fichier CSV.")

    df = df.dropna(subset=["content", "score"])  # Supprimer les lignes avec valeurs manquantes
    df["clean_text"] = df["content"].apply(clean_text)  # Nettoyage
    df["tokens"] = df["clean_text"].apply(lambda x: tokenizer(x, padding="max_length", truncation=True))  # Tokenisation
    df["sentiment"] = df["score"].apply(label_sentiment)  # Attribution des labels

    return df

# Test rapide
if __name__ == "__main__":
    df = pd.read_csv(r'C:\Users\moudi\sentiment-analysis-pipeline\dataset.csv')
    df = preprocess_data(df)
    print(df[["content", "clean_text", "tokens", "sentiment"]].head())
=======
from data_extraction import data  # Importez data 

import re
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from transformers import BertTokenizer

# Importer le dataset depuis data_atraction.py
from data_extraction import data  # Assurez-vous que data_atraction.py contient un DataFrame nommé 'data'

data = data.copy()  # Faire une copie pour éviter de modifier l'original

# Nettoyage du texte
def clean_text(text):
    text = re.sub(r'[^\w\s]', '', str(text))  # Supprimer les caractères spéciaux
    text = text.lower()  # Convertir en minuscules
    text = re.sub(r'\d+', '', text)  # Supprimer les nombres
    return text

data['content'] = data['content'].apply(clean_text)

# Suppression des stop words
stop_words = set(stopwords.words('english'))
def remove_stopwords(text):
    return ' '.join([word for word in text.split() if word not in stop_words])

data['content'] = data['content'].apply(remove_stopwords)

# Lemmatisation
lemmatizer = WordNetLemmatizer()
def lemmatize_text(text):
    return ' '.join([lemmatizer.lemmatize(word) for word in text.split()])

data['content'] = data['content'].apply(lemmatize_text)

# Tokenization avec BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def encode_text(text):
    return tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=128,
        padding='max_length',
        truncation=True,
        return_attention_mask=True,
        return_tensors='pt'
    )

data['encoded'] = data['content'].apply(encode_text)

# Extraction des tokens et des masques d'attention
input_ids = data['encoded'].apply(lambda x: x['input_ids'].squeeze().tolist())
attention_masks = data['encoded'].apply(lambda x: x['attention_mask'].squeeze().tolist())

data['input_ids'] = input_ids
data['attention_mask'] = attention_masks

# Supprimer la colonne encodée intermédiaire
data.drop(columns=['encoded'], inplace=True)

# Sauvegarder le DataFrame prétraité
data.to_csv('preprocessed_dataset.csv', index=False)

import os
print(os.getcwd())  # Affiche le répertoire actuel

>>>>>>> 814322e459e605fbb43a43f362e9785e62f23d5d
