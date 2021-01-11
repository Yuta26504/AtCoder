import io
import sys

_INPUT = """\
box
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
S = input()
print(S+"es" if S[-1] == "s" else S+"s")