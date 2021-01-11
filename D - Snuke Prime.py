import io
import sys

_INPUT = """\
2 6
1 2 4
2 2 4
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------

N, C = map(int, input().split())
abc = []
cost = []
day = []
for i in range(N):
    a, b, c = map(int, input().split())
    day.append(a)
    day.append(b)
    cost.append(c)
    abc.append([a, b, c])
total = [((i[1]-i[0])+1)*i[2] for i in abc]

def search(a, b, c, d):
    if a<=c<=b<=d:
        return c,b

days = search(day[0], day[1], day[2], day[3])
test = (days[1] - days[0]) * cost[0])+((days[1] - days[0]) * cost[1]
if test >= C:

print()