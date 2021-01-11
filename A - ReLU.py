import io
import sys

_INPUT = """\
-10
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
x = int(input())
print(x if x >= 0 else 0)