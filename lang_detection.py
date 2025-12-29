from langdetect import detect_langs, DetectorFactory
from typing import Any

DetectorFactory.seed = 0

def lang_classification(text: str) -> list[Any]:
    """
    Detect languages with probabilities.
    Returns a list of Language objects.
    """
    return detect_langs(text)

def lang_suggestion(text: str) -> list[str]:
    """
    Returns a list of language codes sorted by probability
    """
    return [language.lang for language in lang_classification(text)]

def display_lang(text: str) -> str:
    """
    Formats language suggestions
    Returns f-string that contains results
    """
    languages = lang_suggestion(text)
    if not languages:
        return "Language: unknown"

    if len(languages) == 1:
        return f"Language: {languages[0]}"
    else:
        return f'Language: "{languages[0]}" \n\n (If not, maybe "{languages[1]}" ?)'