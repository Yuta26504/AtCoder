import io
import sys

_INPUT = """\
3
11 13
17 47
359 44683
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N = int(input())

nums = []
for _ in range(N):
    A, B = map(int, input().split())
    total = ((B-A+1)*(A+B))//2
    nums.append(total)

print(sum(nums))