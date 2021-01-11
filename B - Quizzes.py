import io
import sys

_INPUT = """\
20 10
xxxxxxxxxxxxxxxxxxxx
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N, X = map(int, input().split())
S = list(input())
score = X
for i in S:
    if i == "o":
        score += 1
    else:
        if score > 0:
            score -= 1

print(score)