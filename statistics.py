import re
from typing import List
import matplotlib as plt

def compute_stats(text: str) -> List[int]:
    """
    Generates statistics on a given text

    Args:
        text: text to be analyzed

    Returns:
        list of stats
    """
    statistics = []
    text_no_space = [char for char in text if char != " "]
    length_text = len(text_no_space)
    words = text.split()
    num_words = len(words)
    sentences = re.split(r'[\.\?!]+', text)
    num_sentences = len(sentences)
    avg_len = sum(len(w) for w in words) / num_words
    return [length_text, num_words, num_sentences, avg_len]

# def visualize_stats(stats_list: List[int]) -> plt.Figure:
    """
    Generates a Maplotlib graph based on a list of stats from compute_stats()

    Args:

    """

"""Stats: 
Character count: {length_text}
Word count: {num_words}
Sentence count: {num_sentences}
Average word length: {avg_len}
"""

if __name__ == "__main__":
    print(compute_stats("Bonjour je m'appelle Paul. Je suis un mec bien sympathique"))