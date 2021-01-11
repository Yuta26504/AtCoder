import io
import sys

_INPUT = """\
3
1 3 5
3 -6 3

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
total = 0
for a, b in zip(A, B):
    total += a*b

if total == 0:
    print("Yes")
else:
    print("No")