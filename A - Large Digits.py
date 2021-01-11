import io
import sys

_INPUT = """\
100 999

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------

A, B = input().split()
a = 0
b = 0
for i in str(A):
    a += int(i)
for i in str(B):
    b += int(i)

print(max(a, b))
