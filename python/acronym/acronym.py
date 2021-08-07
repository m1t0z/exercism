import re


def abbreviate(phrase: str) -> str:
    return "".join(map(lambda w: w[0].upper(), re.findall(r"[a-zA-Z']+", phrase)))
