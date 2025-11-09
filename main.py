import sys
from divisors import get_divisors

def run():
    s = sys.stdin.read().strip()
    if not s:
        return
    n = int(s)
    ans = get_divisors(n)
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    run()
