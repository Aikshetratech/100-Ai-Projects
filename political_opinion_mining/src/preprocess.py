import re
import string

def clean_text(text):
    """
    Clean tweet text:
    - Lowercase
    - Remove URLs, mentions, hashtags
    - Remove punctuation
    """
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()
    return text
