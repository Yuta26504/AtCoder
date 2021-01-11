import io
import sys

_INPUT = """\
100 100
100 200
100 297
0 0
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
n, x = map(int, input().split())
N = [i+1 for i in range(n)]

while n != 0 or x != 0:
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if N[i]+N[j]+N[k] == x:
                    ans += 1

    print(ans)
    n, x = map(int, input().split())
    N = [i+1 for i in range(n)]
