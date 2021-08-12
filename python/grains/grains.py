_LIMIT = 64


def square(number: int) -> int:
    if not (1 <= number <= _LIMIT):
        raise ValueError(f"Invalid number {number}!")
    return 1 << (number - 1)


# The most optimized implementation
def total() -> int:
    return (1 << _LIMIT) - 1


# Naive implementation: repeating the same multiplications again and again
def _total_impl_1() -> int:
    return sum(square(n + 1) for n in range(0, 64))


# Slightly more optimized implementation
def _iterate_squares():
    square = 1
    yield square
    for n in range(1, _LIMIT):
        square *= 2
        yield square


def _total_impl_2() -> int:
    return sum(_iterate_squares())
