# summarizer.py
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

class MultilingualSummarizer:
    def __init__(self):
        self.model_name = "facebook/mbart-large-50-many-to-one-mmt"
        self.tokenizer = MBart50TokenizerFast.from_pretrained(self.model_name)
        self.model = MBartForConditionalGeneration.from_pretrained(self.model_name)

    def summarize(self, text, lang_code="en_XX"):
        """
        Summarize text in the specified language.
        Supported language codes: en_XX, fr_XX, es_XX, hi_IN, de_DE, etc.
        """
        self.tokenizer.src_lang = lang_code
        inputs = self.tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = self.model.generate(
            **inputs,
            num_beams=4,
            length_penalty=2.0,
            max_length=100,
            min_length=30,
            early_stopping=True
        )
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
