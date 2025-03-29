import pandas as pd
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
)
from src.data_processing import preprocess_data


def load_model_and_tokenizer(model_name):
    """Charge le modèle pré-entraîné et le tokenizer."""
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model


def fine_tune_model(model_name, dataset_path, output_dir="./results"):
    """Affine le modèle sur l'ensemble de données."""
    tokenizer, model = load_model_and_tokenizer(model_name)

    df = pd.read_csv(dataset_path)
    dataset = Dataset.from_pandas(df)
    tokenized_dataset = dataset.map(
        lambda x: preprocess_data(tokenizer, x), batched=True
    )
    train_test_split = tokenized_dataset.train_test_split(test_size=0.1)

    training_args = TrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=3,
        weight_decay=0.01,
        logging_dir=f"{output_dir}/logs",
        logging_steps=10,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_test_split["train"],
        eval_dataset=train_test_split["test"],
    )

    trainer.train()
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    model.config.to_json_file(f"{output_dir}/config.json")

    return trainer
