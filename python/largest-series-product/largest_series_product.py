import math


def largest_product(series: str, size: int) -> int:
    if not (0 <= size <= len(series)):
        raise ValueError("Invalid input!")

    digits = [int(ch) for ch in series]

    chunks_it = (digits[i : i + size] for i in range(0, len(digits) - size + 1))

    return max(math.prod(chunk) for chunk in chunks_it)
