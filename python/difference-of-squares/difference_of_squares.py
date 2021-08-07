def _get_first_n_natural_numbers(n: int):
    return range(1, n + 1)


def square_of_sum(n: int) -> int:
    return sum(_get_first_n_natural_numbers(n)) ** 2


def sum_of_squares(n: int) -> int:
    return sum(map(lambda n: n ** 2, _get_first_n_natural_numbers(n)))


def difference_of_squares(n: int) -> int:
    return square_of_sum(n) - sum_of_squares(n)
