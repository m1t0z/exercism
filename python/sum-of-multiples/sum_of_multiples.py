def sum_of_multiples(limit: int, multiples_of: list[int]) -> int:

    # remove 0
    multiples_of = [m for m in multiples_of if m != 0]

    multiples = set()
    for n in range(1, limit):
        for m in multiples_of:
            if n % m == 0:
                multiples.add(n)
                break

    return sum(multiples)
