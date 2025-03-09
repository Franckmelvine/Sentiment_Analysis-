import torch
import pandas as pd
from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments
from datasets import Dataset
from sklearn.model_selection import train_test_split

def load_data(file_path):
    df = pd.read_csv(file_path)
    df = df[['content', 'score']].dropna()
    df['score'] = df['score'] - 1  # Transformer les labels en 0-4 si c'est sur 1-5
    return df

def tokenize_function(examples):
    return tokenizer(examples['content'], padding='max_length', truncation=True)

# Charger les données
data_path = 'reviews.csv'  # Modifier avec le chemin correct
df = load_data(data_path)

# Diviser en train et test
train_texts, test_texts, train_labels, test_labels = train_test_split(
    df['content'].tolist(), df['score'].tolist(), test_size=0.2, random_state=42
)

# Convertir en Dataset Hugging Face
train_dataset = Dataset.from_dict({'content': train_texts, 'score': train_labels})
test_dataset = Dataset.from_dict({'content': test_texts, 'score': test_labels})

# Charger le modèle et le tokenizer
model_name = 'nlptown/bert-base-multilingual-uncased-sentiment'  # Modèle BERT pré-entraîné
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=5)

# Tokenization
tokenized_train = train_dataset.map(tokenize_function, batched=True)
tokenized_test = test_dataset.map(tokenize_function, batched=True)

# Définir les arguments d'entraînement
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy='epoch',
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir='./logs',
)

# Initialiser le Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train,
    eval_dataset=tokenized_test,
)

# Entraîner le modèle
trainer.train()

# Sauvegarder le modèle
tokenizer.save_pretrained('./saved_model')
model.save_pretrained('./saved_model')
