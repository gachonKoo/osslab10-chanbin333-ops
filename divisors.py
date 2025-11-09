import sys

def get_divisors(n: int):
    if n <= 0:
        return []
    return [d for d in range(1, n + 1) if n % d == 0]

def main():
    if len(sys.argv) >= 2:
        n = int(sys.argv[1])
    else:
        s = sys.stdin.read().strip()
        n = int(s) if s else 0
    print(" ".join(map(str, get_divisors(n))))

if __name__ == "__main__":
    main()
