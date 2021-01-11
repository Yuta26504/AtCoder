import io
import sys

_INPUT = """\
5 5
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
road = [i for i in range(1, N)]
prm = list(itertools.permutations(road))

counter = 0
for i in prm:
    total = T[0][i[0]]
    for j in range(N-2):
        total += T[i[j]][i[j+1]]
    total += T[i[N-2]][0]
    if total == K:
        counter += 1

print(counter)
