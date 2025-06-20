from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

def load_model(model_path="google/flan-t5-base"):
    print("🔄 Loading Flan-T5 Base model... (This may take a minute on first run)")

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

    print("✅ Model loaded successfully! Using CPU.")
    return pipeline("text2text-generation", model=model, tokenizer=tokenizer)
