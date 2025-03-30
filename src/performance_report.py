import json
import os


def generate_report(metrics_path="metrics.json"):
    if not os.path.exists(metrics_path):
        print("❌ Le fichier metrics.json est introuvable.")
        return

    with open(metrics_path, "r") as f:
        try:
            metrics = json.load(f)
        except json.JSONDecodeError:
            print("❌ Erreur de lecture du fichier metrics.json.")
            return

    print("📊 Rapport de performance :")
    for key, val in metrics.items():
        try:
            formatted = f"{val:.2%}" if isinstance(val, float) else val
            print(f"- {key.capitalize()} : {formatted}")
        except Exception as e:
            print(f"- {key.capitalize()} : {val} (⚠️ Format non reconnu)")


if __name__ == "__main__":
    generate_report()
