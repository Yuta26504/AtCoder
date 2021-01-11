import io
import sys

_INPUT = """\
10000 0
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
A, B = map(int, input().split())
print((2*A+100)-B)