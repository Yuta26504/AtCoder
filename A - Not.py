import io
import sys

_INPUT = """\
0
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
print(0 if int(input()) == 1 else 1)
