import io
import sys

_INPUT = """\
10
red
red
red
!orange
yellow
!blue
cyan
!green
brown
!gray
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------

N = int(input())
S = set([input() for _ in range(N)])

for i in S:
    if i[0] == "!":
        if i[1:] in S:
            print(i[1:])
            exit()
print("satisfiable")
    