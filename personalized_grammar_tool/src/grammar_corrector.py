from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class GrammarCorrector:
    def __init__(self):
        print("🔤 Loading grammar correction model...")
        self.tokenizer = AutoTokenizer.from_pretrained("prithivida/grammar_error_correcter_v1")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("prithivida/grammar_error_correcter_v1")

    def correct(self, sentence: str) -> str:
        inputs = self.tokenizer.encode(sentence, return_tensors="pt", max_length=128, truncation=True)
        outputs = self.model.generate(inputs, max_length=128, num_beams=5, early_stopping=True)
        corrected = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return corrected
