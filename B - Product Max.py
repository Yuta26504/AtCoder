import io
import sys

_INPUT = """\
-1000000000 0 -1000000000 0
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
a, b, c, d = map(int, input().split())

max_list = [a*c, a*d, b*c, b*d]
print(max(max_list))
