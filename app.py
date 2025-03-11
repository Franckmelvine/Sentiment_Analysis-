import streamlit as st
from transformers import pipeline

# Titre de l'application
st.title("Analyse de Sentiments avec BERT")

# Charger le modèle une seule fois au démarrage de l'application
@st.cache_resource
def load_model():
    model_name = "arindamatcalgm/w266_model4_BERT_AutoModelForSequenceClassification"
    return pipeline("text-classification", model=model_name)

# Définir un mapping des labels pour des résultats compréhensibles
label_mapping = {
    "LABEL_0": "Négatif",
    "LABEL_1": "Positif",
}

# Ajouter des émoticônes pour rendre l'interface plus conviviale
sentiment_emojis = {
    "Positif": "😊",
    "Négatif": "😠",
    "Inconnu": "❓",
}

# Fonction pour prédire le sentiment
def predict_sentiment(pipe, text):
    result = pipe(text)[0]  # Récupérer le premier résultat
    label = result['label']
    score = result['score']
    # Remplacer le label par une description compréhensible
    sentiment = label_mapping.get(label, "Inconnu")
    return sentiment, score

# Charger le modèle
pipe = load_model()

# Zone de texte pour l'entrée utilisateur
user_input = st.text_area("Entrez votre texte ici pour analyser le sentiment :", "")

# Bouton pour lancer l'analyse
if st.button("Analyser"):
    if user_input:
        # Faire la prédiction
        sentiment, confidence = predict_sentiment(pipe, user_input)

        # Afficher les résultats avec des émoticônes
        st.write(f"**Sentiment :** {sentiment} {sentiment_emojis.get(sentiment, '')}")
        st.write(f"**Confiance :** {confidence:.4f}")

        # Afficher un message d'avertissement si le sentiment est inconnu
        if sentiment == "Inconnu":
            st.warning(f"Le label renvoyé par le modèle n'est pas reconnu. Veuillez vérifier le modèle.")
    else:
        st.warning("Veuillez entrer un texte pour l'analyse.")