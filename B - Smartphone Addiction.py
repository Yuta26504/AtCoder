import io
import sys

_INPUT = """\
20 1 30
1 10
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N, M, T = map(int, input().split())
remain = N
time = 0
for _ in range(M):
    A, B = map(int, input().split())
    remain -= (A - time)
    charge = B - A
    if remain > 0:
        remain += charge
        if remain > N:
            remain = N
        time = B
    else:
        print("No")
        exit()
remain -= (T - time)
if remain > 0:
    print("Yes")
else:
    print("No")



