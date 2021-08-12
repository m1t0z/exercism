def primes(limit: int) -> list[int]:
    is_prime_arr = [True for _ in range(limit + 1)]

    prime = 2

    while prime < len(is_prime_arr):
        if is_prime_arr[prime]:
            x = prime * 2
            while x < len(is_prime_arr):
                is_prime_arr[x] = False
                x += prime
        prime += 1

    return [i for i, is_prime in enumerate(is_prime_arr) if i >= 2 and is_prime]
