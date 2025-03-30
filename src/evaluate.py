# evaluate.py

import json
from sklearn.metrics import accuracy_score

# Remplacer par tes vraies prédictions plus tard
y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 1, 0, 0]

accuracy = accuracy_score(y_true, y_pred)

# Sauvegarde du score dans un fichier
with open("metrics.json", "w") as f:
    json.dump({"accuracy": accuracy}, f)

# Échoue si en dessous du seuil
if accuracy < 0.75:
    raise ValueError(f"Accuracy trop faible ({accuracy:.2f}) : échec de l'évaluation.")
