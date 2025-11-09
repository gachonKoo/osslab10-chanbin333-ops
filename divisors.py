def get_divisors(n: int):
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n <= 0:
        return []
    return [d for d in range(1, n + 1) if n % d == 0]

def divisors(n: int):
    return get_divisors(n)

def factors(n: int):
    return get_divisors(n)
