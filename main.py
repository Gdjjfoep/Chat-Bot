from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("./flan_base_local")
model = AutoModelForSeq2SeqLM.from_pretrained("./flan_base_local")
pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
