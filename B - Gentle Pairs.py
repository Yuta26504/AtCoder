import io
import sys

_INPUT = """\
10
-31 -35
8 -36
22 64
5 73
-14 8
18 -58
-41 -85
1 -88
-21 -85
-11 82

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
import itertools

N = int(input())
x = [list(map(int, input().split())) for _ in range(N)]
x = itertools.combinations(x, 2)

count = 0
for i in x:
    gradient = (i[1][1]-i[0][1]) / (i[1][0]-i[0][0])
    if -1 <= gradient <= 1:
        count += 1
print(count)
