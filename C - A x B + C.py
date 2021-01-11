import io
import sys

_INPUT = """\
1000000
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N = int(input())

ans = 0
for a in range(1, N):
    ans += (N-1)//a
print(ans)
