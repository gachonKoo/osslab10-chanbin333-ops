import sys
try:
    from divisors import get_divisors as _gd
except Exception:
    def _gd(n: int):
        if not isinstance(n, int):
            raise TypeError("n must be int")
        if n <= 0:
            return []
        return [d for d in range(1, n + 1) if n % d == 0]

def get_divisors(n: int):
    return _gd(n)

def run():
    data = sys.stdin.read().strip()
    if not data:
        return
    n = int(data)
    ans = _gd(n)
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    run()
