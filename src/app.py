import streamlit as st
from transformers import pipeline
import matplotlib.colors as mcolors
import numpy as np

# Configuration de la page
st.set_page_config(page_title="Analyse de Sentiments", layout="wide")

# Titre de l'application avec emoji
st.title("🧠 Analyse de Sentiments avec BERT")

# Charger le modèle de manière optimisée
@st.cache_resource(show_spinner="Chargement du modèle...")
def load_model():
    model_name = (
        "arindamatcalgm/w266_model4_BERT_AutoModelForSequenceClassification"
    )
    return pipeline("text-classification", model=model_name, device="cpu")


# Mapping des labels et emojis
LABEL_CONFIG = {
    "LABEL_0": {
        "display": "Négatif",
        "emoji": "😠",
        "base_color": "#FF0000"
    },
    "LABEL_1": {
        "display": "Positif",
        "emoji": "😊",
        "base_color": "#00FF00"
    }
}


# Fonction pour générer un dégradé de couleur
def get_color(score, base_color):
    rgb = mcolors.hex2color(base_color)
    intensity = 0.3 + 0.7 * score
    return f"rgb({int(rgb[0]*255*intensity)}, {int(rgb[1]*255*intensity)}, {int(rgb[2]*255*intensity)})"


# Fonction d'analyse de sentiment améliorée
def analyze_sentiment(pipe, text):
    try:
        result = pipe(text, truncation=True, max_length=512)[0]
        label_info = LABEL_CONFIG.get(result["label"], {
            "display": "Inconnu",
            "emoji": "❓",
            "base_color": "#808080"
        })

        return {
            "sentiment": label_info["display"],
            "emoji": label_info["emoji"],
            "confidence": result["score"],
            "color": get_color(result["score"], label_info["base_color"])
        }

    except Exception as e:
        st.error(f"Erreur lors de l'analyse: {str(e)}")
        return None


# Interface utilisateur
with st.container():
    st.subheader("Testez notre analyseur de sentiments")
    user_input = st.text_area(
        "Entrez votre texte ici:",
        "",
        height=150,
        placeholder="Ex: Je suis très heureux d'utiliser cette application !"
    )

    col1, col2 = st.columns([1, 3])
    with col1:
        analyze_btn = st.button("Analyser le sentiment", use_container_width=True)
    with col2:
        st.caption("Appuyez sur le bouton pour analyser le texte")


# Chargement du modèle (se fait une seule fois)
pipe = load_model()


# Traitement lors du clic
if analyze_btn and user_input:
    with st.spinner("Analyse en cours..."):
        result = analyze_sentiment(pipe, user_input)

    if result:
        st.markdown(
            f"""
            <div style='
                background-color: {result["color"]}20;
                border-left: 5px solid {result["color"]};
                padding: 1rem;
                border-radius: 0.5rem
