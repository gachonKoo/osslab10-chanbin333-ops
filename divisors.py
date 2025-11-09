def get_divisors(n: int):
    if n <= 0:
        return []
    return [d for d in range(1, n + 1) if n % d == 0]
