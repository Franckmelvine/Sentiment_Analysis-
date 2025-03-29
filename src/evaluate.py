import json
from sklearn.metrics import accuracy_score

# Exemples simulés – remplace-les par de vraies valeurs si dispo
y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 1, 0, 0]

acc = accuracy_score(y_true, y_pred)

# Sauvegarde dans un fichier JSON
with open("metrics.json", "w") as f:
    json.dump({"accuracy": acc}, f)

# Si la performance est trop faible, on échoue
if acc < 0.75:
    raise ValueError("Accuracy trop faible : échec de l'évaluation.")
