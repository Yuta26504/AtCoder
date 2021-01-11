import io
import sys

_INPUT = """\
10000 1 1
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
D, T, S = map(int, input().split())

dis= S*T
if D > dis:
    print("No")
else:
    print("Yes")