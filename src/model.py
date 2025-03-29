def fine_tune_model(model_name, dataset_path, output_dir="./results"):
    """Affine le modèle sur l'ensemble de données."""
    tokenizer, model = load_model_and_tokenizer(model_name)
    
    # Charger et prétraiter le dataset
    df = pd.read_csv(dataset_path)
    dataset = Dataset.from_pandas(df)
    tokenized_dataset = dataset.map(lambda x: preprocess_data(tokenizer, x), batched=True)
    train_test_split = tokenized_dataset.train_test_split(test_size=0.1)
    
    # Paramètres d'entraînement
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
    
    # Initialisation du Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_test_split['train'],
        eval_dataset=train_test_split['test'],
    )
    
    # Entraînement du modèle
    trainer.train()

    # Sauvegarde du modèle et du tokenizer
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    
    # Sauvegarde de la configuration manuellement
    model.config.to_json_file(f"{output_dir}/config.json")

    return trainer
