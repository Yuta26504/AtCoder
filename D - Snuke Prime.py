import io
import sys

_INPUT = """\
5 100000
583563238 820642330 44577
136809000 653199778 90962
54601291 785892285 50554
5797762 453599267 65697
468677897 916692569 87409
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------

from collections import defaultdict

N, C = map(int, input().split())
d = defaultdict(int)

for _ in range(N):
    a, b, c = map(int, input().split())
    d[a] += c
    d[b+1] -= c
ans = 0
cost = 0
before = 0
for now in sorted(d):
    ans += min(cost, C) * (now - before) # お金×日数
    cost += d[now]
    before = now
print(ans)