import io
import sys

_INPUT = """\
869121

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N = int(input())
mod = pow(10, 9) + 7

a = pow(10, N, mod)
b = pow(9, N, mod)
c = pow(9, N, mod)
d = pow(8, N, mod)

ans = (a-b-c+d)%mod
print(ans)

# 包除原理
# https://cyclo-commuter.hatenablog.jp/entry/2019/08/01/162125