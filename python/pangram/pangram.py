import string

_alphabet = set(string.ascii_lowercase)


def is_pangram(sentence: str) -> bool:
    return _alphabet.issubset(sentence.lower())
