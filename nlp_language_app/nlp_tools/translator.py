from googletrans import Translator
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

translator = Translator()

def translate_text(text, dest_lang="en"):
    """
    Translate text to the destination language.
    """
    translated = translator.translate(text, dest=dest_lang)
    return translated.text

def get_word_info(text):
    """
    Return definitions and synonyms.
    If text is a sentence, show info for the first word.
    """
    tokens = [w.lower() for w in word_tokenize(text) if w.isalpha()]
    if not tokens:
        return {"definitions": [], "synonyms": []}
    
    word = tokens[0]  # take first meaningful word
    synsets = wordnet.synsets(word)
    definitions = [syn.definition() for syn in synsets]
    synonyms = [lemma.name() for syn in synsets for lemma in syn.lemmas()]
    return {"definitions": definitions[:3], "synonyms": list(set(synonyms))[:5]}
