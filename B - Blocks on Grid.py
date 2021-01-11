import io
import sys

_INPUT = """\
3 2
4 4
4 4
4 4
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
import itertools

H, W = map(int, input().split())
a = [map(int, input().split()) for _ in range(H)]
A = list(itertools.chain.from_iterable(list(i) for i in a))

ans = 0
if max(A) - min(A) == 0:
    print(ans)
    exit()
else:
    for i in A:
        ans += i-min(A)

print(ans)