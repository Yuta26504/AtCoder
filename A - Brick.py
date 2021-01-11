import io
import sys

_INPUT = """\
1000 1

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N, W = map(int, input().split())

print(N//W)
