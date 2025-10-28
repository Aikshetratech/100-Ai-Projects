import json
from textblob import TextBlob
from pathlib import Path

class Personalizer:
    def __init__(self, data_path="data/user_mistakes.json"):
        self.path = Path(data_path)
        self.path.parent.mkdir(exist_ok=True)
        if not self.path.exists():
            self.path.write_text(json.dumps({}, indent=4))
        self.mistakes = json.loads(self.path.read_text())

    def analyze_and_save(self, original: str, corrected: str):
        diff = self._find_diff(original, corrected)
        if diff:
            print(f"🧩 Detected improvement: {diff}")
            for mistake, fix in diff.items():
                self.mistakes[mistake] = fix
            self._save()

    def _find_diff(self, original: str, corrected: str):
        diff = {}
        o_words, c_words = original.split(), corrected.split()
        for o, c in zip(o_words, c_words):
            if o != c:
                diff[o] = c
        return diff if diff else None

    def _save(self):
        self.path.write_text(json.dumps(self.mistakes, indent=4))

    def personalize(self, sentence: str) -> str:
        words = sentence.split()
        for i, w in enumerate(words):
            if w in self.mistakes:
                words[i] = self.mistakes[w]
        return " ".join(words)
