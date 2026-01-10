import pytest
import matplotlib.pyplot as plt
from statistics import compute_stats, visualize_stats, top_words

def test_compute_stats():
    "Tests various stat computations"
    text = "Bonjour tout le monde! Je suis une petite grenouille à chapeau. Je fais des sauts de nénuphar en nénuphar."
    stats = compute_stats(text)

    assert isinstance(stats, dict)
    assert stats["Word count"] == 19
    assert stats["Sentence count"] == 3
    assert stats["Character count (no spaces)"] == 88

def test_compute_stats_void():
    "Tests what happens if compute_stats has an empty input"
    text = ""
    stats = compute_stats(text)
    assert isinstance(stats, dict)

def test_visualize_stats():
    "Tests that the return is a matplotlib figure"
    stats = {
        "Word count": 10,
        "Sentence count": 2
    }
    fig = visualize_stats(stats)
    assert isinstance(fig, plt.Figure)

def test_visualize_stats_empty_dict():
    "Tests that an empty dict returns an error"
    empty_dict = {}
    with pytest.raises(ValueError) as exc_info:
        visualize_stats(empty_dict)