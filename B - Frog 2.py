import io
import sys

_INPUT = """\
10 4
40 10 20 70 80 10 20 70 80 60

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------
N, K = map(int, input().split())
H = list(map(int, input().split()))

DP = [0]
for i in range(N-1):
    act = float("inf")
    for k in range(K):
        if i-k < 0:
            continue
        act = min(DP[-1-k] + abs(H[i-k]-H[i+1]), act)
    DP.append(act)

print(DP[-1])