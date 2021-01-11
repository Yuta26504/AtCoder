import io
import sys

_INPUT = """\
4
4
4
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------
a, b, h = [int(input()) for _ in range(3)]

print((a+b)*h//2)

