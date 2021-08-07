def is_isogram(string: str) -> bool:

    history = set()
    for letter in map(str.lower, filter(str.isalpha, string)):
        if letter in history:
            return False
        history.add(letter)

    return True
