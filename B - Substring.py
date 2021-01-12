import io
import sys

_INPUT = """\
codeforces
atcoder

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
S = input()
T = input()
ans = []
for i in range(len(S)-len(T)+1):
    num = 0
    for j in range(len(T)):
        if S[i+j] != T[j]:
            num += 1
        else:
            pass
    ans.append(num)

print(min(ans))
    