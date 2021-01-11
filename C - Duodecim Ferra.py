import io
import sys

_INPUT = """\
17
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
L = int(input())

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

def cmb(n, r):
    if n == r:
        return 1
    return fact(n)//(fact(n-r)*fact(r))

print(cmb(L-1, 11))