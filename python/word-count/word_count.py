import collections
import re


def count_words(sentence: str) -> dict[str, int]:
    words = map(lambda w: w.strip("'").lower(), re.findall(r"[a-zA-Z0-9']+", sentence))
    return collections.Counter(words)
