def is_valid(isbn: str) -> bool:

    factor = 10
    res = 0

    # Verify in a single loop-pass.
    for ch in isbn:
        if ch.isdigit():
            if factor == 0:
                return False
            res += int(ch) * factor
            factor -= 1
        elif ch == "X":
            if factor != 1:
                return False
            res += 10 * factor
            factor -= 1
        elif ch != "-":
            return False

    return factor == 0 and res % 11 == 0
