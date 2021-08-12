import string

_PLAIN = string.ascii_lowercase
_CIPHER = string.ascii_lowercase[::-1]
_IGNORED = ",. "
_CIPHER_GROUP_LEN = 5

_PLAIN_TO_CIPHER = str.maketrans(_PLAIN, _CIPHER, _IGNORED)
_CIPHER_TO_PLAIN = str.maketrans(_CIPHER, _PLAIN, _IGNORED)


def encode(plain_text: str) -> str:
    encoded = plain_text.lower().translate(_PLAIN_TO_CIPHER)
    groups = (
        encoded[i : i + _CIPHER_GROUP_LEN]
        for i in range(0, len(encoded), _CIPHER_GROUP_LEN)
    )
    return " ".join(groups)


def decode(ciphered_text: str) -> str:
    return ciphered_text.lower().translate(_CIPHER_TO_PLAIN)
