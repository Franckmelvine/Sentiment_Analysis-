import unittest
from inference import predict_sentiment

class TestInference(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test."""
        self.model_path = "./results"  # Modifier selon l'emplacement du modèle
    
    def test_prediction_output(self):
        """Teste si l'inférence retourne un label et un score valides."""
        sample_text = "J'adore ce produit, il est génial !"
        
        # Effectuer la prédiction
        result = predict_sentiment(self.model_path, sample_text)
        
        # Vérifications
        self.assertIn("label", result, "Le résultat doit contenir un label.")
        self.assertIn("score", result, "Le résultat doit contenir un score.")
        self.assertIsInstance(result["label"], str, "Le label doit être une chaîne de caractères.")
        self.assertIsInstance(result["score"], float, "Le score doit être un nombre à virgule flottante.")
        self.assertGreaterEqual(result["score"], 0.0, "Le score doit être supérieur ou égal à 0.")
        self.assertLessEqual(result["score"], 1.0, "Le score doit être inférieur ou égal à 1.")

if __name__ == "__main__":
    unittest.main()
