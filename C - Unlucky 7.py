import io
import sys

_INPUT = """\
100000
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N = int(input())
ans = 0

for i in range(1, N+1):
    if ("7" not in str(i)) and ("7" not in str(oct(i)[2:])):
        ans += 1
    else:
        pass

print(ans)
