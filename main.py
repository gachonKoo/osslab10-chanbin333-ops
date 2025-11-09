import sys
s = sys.stdin.read().strip()
n = int(s)
ans = [str(d) for d in range(1, n + 1) if n % d == 0]
print(" ".join(ans))
