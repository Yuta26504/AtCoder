import io
import sys

_INPUT = """\
4
6 13 12 5 3 7 10 11 16 9 8 15 2 1 14 4

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N = int(input())
A = list(map(int, input().split()))
A_copy = A.copy()

for j in range(pow(2, N)-1):
    if len(A) > 2:
        play1 = A.pop(0)
        play2 = A.pop(0)
        A.append(max([play1, play2]))
    else:
        print(A_copy.index(min(A))+1)