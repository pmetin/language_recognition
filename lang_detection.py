from langdetect import detect_langs, DetectorFactory
from typing import Any, List

DetectorFactory.seed = 0

def lang_classification(text: str) -> List[Any]:
    """
    Detect languages with probabilities

    Args:
        text: text to be analyzed

    Returns:
        list of Language objects.
    """
    try:
        return detect_langs(str(text))
    except Exception:
        return "Try adding a couple letters maybe?"


def lang_suggestion(text: str) -> List[str]:
    """
    Returns a list of language codes sorted by probability for a given text processed by lang_classification

    Args:
        text: text to be analyzed
    
    Returns:
        list of language codes
    """
    languages = lang_classification(text)
    if type(languages) == str:
        return languages
    suggestion = [l.lang for l in languages]
    return suggestion

def display_lang(text: str) -> str:
    """
    Formats language suggestions

    Args:
        text: text to be analyzed
    
    Returns:
        f-string that contains results
    """
    languages = lang_suggestion(text)

    if type(languages) == str:
        return languages
    elif not languages:
        return "Language: unknown"
    elif len(languages) == 1:
        return f"Language: {languages[0]}"
    else:
        return f'Language: "{languages[0]}" \n\n (If not, maybe "{languages[1]}" ?)'