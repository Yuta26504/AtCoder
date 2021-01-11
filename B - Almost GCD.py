import io
import sys

_INPUT = """\
3
3 12 7

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N = int(input())
A = sorted(map(int, input().split()))

ans = 0
GCD = 0
for i in range(2, 1001):
    gcd = 0
    for j in A:
        if j%i == 0:
            gcd += 1
    if GCD <= gcd:
        GCD = gcd
        ans = i
print(ans)
    
