import io
import sys

_INPUT = """\
9
8 2
2 3
1 3
3 7
1 0
8 8
5 6
9 7
0 1

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
import itertools
N = int(input())
pos = [tuple(map(int, input().split())) for _ in range(N)]

for i in itertools.combinations(pos, 3):
    Xb = i[1][0] - i[0][0]
    Xc = i[2][0] - i[0][0]
    Yb = i[1][1] - i[0][1]
    Yc = i[2][1] - i[0][1]
    if Xb*Yc == Xc*Yb:
        print("Yes")
        exit()

print("No")