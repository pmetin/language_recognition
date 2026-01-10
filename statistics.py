import re
from typing import List, Dict
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

def compute_stats(text: str) -> Dict:
    """
    Generates statistics on a given text

    Args:
        text: text to be analyzed

    Returns:
        dictionary containing stats
    """
    statistics = []
    text_no_space = [char for char in text if char != " "]
    length_text = len(text_no_space)
    words = text.split()
    num_words = len(words)
    sentences = re.split(r'[\.\?!]+', text)
    num_sentences = len(sentences)
    avg_len = sum(len(w) for w in words) / num_words
    return {
        "Character count (no spaces)": length_text,
        "Word count": num_words,
        "Sentence count": num_sentences, 
        "Average word length": avg_len
    }

def visualize_stats(stats_dict: Dict) -> plt.Figure:
    """
    Generates a Maplotlib graph based on a dictionary of stats from compute_stats()

    Args:
        stats_dict (Dict): dictionary of stats
    
    Returns:
        graph (plt.Figure): graph showcasing the stats
    """
    labels = list(stats_dict.keys())
    values = list(stats_dict.values())

    fig, ax = plt.subplots(figsize=(8,5))

    ax.bar(labels, values, color='skyblue')
    ax.set_title("Text stats")
    ax.set_ylabel("Values")
    ax.set_ylim(0, max(values)*1.2)

    for i, v in enumerate(values):
        ax.text(i, v + max(values)*0.02, str(round(v,2)), ha='center', va='bottom')
    
    plt.tight_layout()
    return fig

def top_words(text: str, n: int = 10) -> pd.DataFrame:
    """
    Computes "n" most frequent words in a text

    Args:
        text (str): text to be processed
        n (int): number of top words to return

    Returns:
        pd.DataFrame: DataFrame that contains the "n" top words and their frequency
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', "", text)
    words = text.split()

    counter = Counter(words)
    most_common = counter.most_common(n)
    df = pd.DataFrame(most_common, columns=["Word", "Frequency"])
    return df