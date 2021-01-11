import io
import sys

_INPUT = """\
1 2
3 4
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
a, b = map(int, input().split())
c, d = map(int, input().split())

print(a*d-b*c)