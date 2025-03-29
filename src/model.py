from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
import torch

def load_model_and_tokenizer():
    """Charge le modèle et le tokenizer."""
    model_name = "arindamatcalgm/w266_model4_BERT_AutoModelForSequenceClassification"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model

def preprocess_data(tokenizer, examples):
    """Tokenise les données textuelles."""
    return tokenizer(examples['content'], padding="max_length", truncation=True)

def fine_tune_model(tokenizer, model, dataset):
    """Affine le modèle sur l'ensemble de données."""
    # Tokeniser le dataset
    tokenized_dataset = dataset.map(lambda x: preprocess_data(tokenizer, x), batched=True)

    # Diviser le dataset en train et test
    train_test_split = tokenized_dataset.train_test_split(test_size=0.1)
    train_dataset = train_test_split['train']
    test_dataset = train_test_split['test']

    # Définir les arguments d'entraînement
    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=3,
        weight_decay=0.01,
    )

    # Définir le Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
    )

    # Affiner le modèle
    trainer.train()
    return trainer

if __name__ == "__main__":
    # Charger le modèle et le tokenizer
    tokenizer, model = load_model_and_tokenizer()

    # Charger votre dataset (supposons que vous avez un DataFrame pandas `df`)
    import pandas as pd
    df = pd.read_csv(r"C:\Users\mouke\Documents\aivancity\PGE3\Semestre 2\MLOps\dataset.csv")  # Remplacez par le chemin de votre dataset
    dataset = Dataset.from_pandas(df)

    # Affiner le modèle
    fine_tune_model(tokenizer, model, dataset)