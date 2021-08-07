_CP_a = ord("a")
_CP_z = ord("z")
_CP_A = ord("A")
_CP_Z = ord("Z")
_ALPHABET_SIZE = 26
assert _ALPHABET_SIZE == (_CP_z - _CP_a + 1) == (_CP_Z - _CP_A + 1)


def _rotate_character(ch: str, key: int) -> str:
    cp = ord(ch)
    if _CP_a <= cp <= _CP_z:
        return chr((cp + key - _CP_a) % _ALPHABET_SIZE + _CP_a)
    elif _CP_A <= cp <= _CP_Z:
        return chr((cp + key - _CP_A) % _ALPHABET_SIZE + _CP_A)
    else:
        return ch


def rotate(text: str, key: int) -> str:
    return "".join(_rotate_character(ch, key) for ch in text)
