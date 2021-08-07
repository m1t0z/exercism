def _iterate_digits(number: int):
    assert number >= 0

    if number == 0:
        yield 0
    else:
        while number != 0:
            yield number % 10
            number = int(number / 10)


def is_armstrong_number(number: int) -> bool:
    digits = list(_iterate_digits(number))
    cnt_digits = len(digits)
    return number == sum(map(lambda d: d ** cnt_digits, digits))
