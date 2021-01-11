import io
import sys

_INPUT = """\
519437318400
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N = int(input())

base = [[i, N//i] for i in range(1, round(N**0.5 + 1)) if N%i == 0]
ans = []
for i in base:
    ans.append(i[0])
    ans.append(i[1])
print(*sorted(set(ans)), sep="\n")