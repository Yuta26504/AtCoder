import io
import sys

_INPUT = """\
12 15

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
point = list(map(int, input().split()))

if min(point)+3 > max(point):
    print("Yes")
else:
    print("No")
