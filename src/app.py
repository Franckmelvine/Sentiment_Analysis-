import streamlit as st
from transformers import pipeline
import matplotlib.colors as mcolors


st.set_page_config(page_title="Analyse de Sentiments", layout="wide")
st.title("🧠 Analyse de Sentiments avec BERT")


@st.cache_resource(show_spinner="Chargement du modèle...")
def load_model():
    model_name = (
        "arindamatcalgm/w266_model4_BERT_"
        "AutoModelForSequenceClassification"
    )
    return pipeline("text-classification", model=model_name, device="cpu")


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


def get_color(score, base_color):
    rgb = mcolors.hex2color(base_color)
    intensity = 0.3 + 0.7 * score
    r, g, b = [int(c * 255 * intensity) for c in rgb]
    return f"rgb({r}, {g}, {b})"


def analyze_sentiment(pipe, text):
    try:
        result = pipe(text, truncation=True, max_length=512)[0]
        label_info = LABEL_CONFIG.get(
            result["label"],
            {
                "display": "Inconnu",
                "emoji": "❓",
                "base_color": "#808080"
            }
        )
        return {
            "sentiment": label_info["display"],
            "emoji": label_info["emoji"],
            "confidence": result["score"],
            "color": get_color(result["score"], label_info["base_color"])
        }
    except Exception as e:
        st.error(f"Erreur lors de l'analyse : {str(e)}")
        return None


with st.container():
    st.subheader("Testez notre analyseur de sentiments")
    user_input = st.text_area(
        "Entrez votre texte ici :",
        "",
        height=150,
        placeholder="Ex : Je suis très heureux d'utiliser cette application !"
    )

    col1, col2 = st.columns([1, 3])
    with col1:
        analyze_btn = st.button(
            "Analyser le sentiment",
            use_container_width=True
        )
    with col2:
        st.caption("Appuyez sur le bouton pour analyser le texte")


pipe = load_model()

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
                border-radius: 0.5rem;
                margin: 1rem 0;
            '>
                <h3 style='color: {result["color"]}'>
                    {result["sentiment"]} {result["emoji"]}
                </h3>
                <p>Confiance : <strong>{result['confidence']:.1%}</strong></p>
            </div>
            """,
            unsafe_allow_html=True  
        )

        st.markdown(
            f"""
            <style>
                .stProgress > div > div > div > div {{
                    background-color: {result["color"]};
                }}
            </style>
            """,
            unsafe_allow_html=True
        )
        st.progress(result["confidence"])

elif analyze_btn and not user_input:
    st.warning("⚠️ Veuillez entrer un texte à analyser")


with st.expander("ℹ️ À propos de cette application"):
    st.markdown(
        """
        Cette application utilise un modèle BERT finetuné pour analyser
        le sentiment d'un texte.
        - 😊 **Positif** : Le texte exprime une émotion positive
        - 😠 **Négatif** : Le texte exprime une émotion négative
        - L'intensité de la couleur correspond au niveau de confiance
          du modèle.
        """
    )
