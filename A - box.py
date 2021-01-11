import io
import sys

_INPUT = """\
100 1 1

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N, A, B = map(int, input().split())
print(N-A+B)