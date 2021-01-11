import io
import sys

_INPUT = """\
5
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N = int(input())

print("White" if N%2==0 else "Black")
