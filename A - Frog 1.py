import io
import sys

_INPUT = """\
6
30 10 60 10 60 50
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------
N = int(input())
H = list(map(int, input().split()))

DP = [0, abs(H[1]-H[0])]
for i in range(N-2):
    DP.append(min(DP[-2] + abs(H[i]-H[i+2]), DP[-1] + abs(H[i+1]-H[i+2])))

print(DP[-1])