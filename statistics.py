import re

def stats(text: str) -> str:
    """
    Generates statistics on a given text
    Returns f-string that contains results
    """
    length_text = len(text)
    words = text.split()
    num_words = len(words)
    sentences = re.split(r'[\.\?!]+', text)
    num_sentences = len(sentences)
    avg_len = sum(len(w) for w in words / num_words)

    return f"""Stats: 
Character count: {length_text}
Word count: {num_words}
Sentence count: {num_sentences}
Average word length: {avg_len}
"""


