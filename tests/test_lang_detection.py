import pytest
from lang_detection import lang_suggestion, display_lang

def test_french():
    "Tests whether lang_suggestion() guesses a basic French input right"
    text = "Bonjour les amis"
    result = lang_suggestion(text)
    assert 'fr' in result

def test_english():
    "Tests whether lang_suggestion() guesses a basic English input right"
    text = "Hello world"
    result = lang_suggestion(text)
    assert 'en' in result

def test_number():
    "Tests whether the behaviour of display_lang works when the input is an integer"
    text = 2
    result = display_lang(text)
    assert 'Try adding a couple letters maybe?'
