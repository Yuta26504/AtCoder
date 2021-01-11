import io
import sys

_INPUT = """\
2
2 -1
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N = int(input())
x = list(map(int, input().split()))

Manhattan = 0
Euclidean = 0
Chebyshev = []
for i in x:
    Manhattan += abs(i)
    Euclidean += abs(i)**2
    Chebyshev.append(abs(i))

print(Manhattan)
print(Euclidean**(0.5))
print(max(Chebyshev))


