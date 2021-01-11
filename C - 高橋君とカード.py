import io
import sys

_INPUT = """\
4 8
7 9 8 9
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N, A = map(int, input().split())
x = list(map(int, input().split()))
X = [i - A for i in x]
X_max = max(x)
dp = [[0]*(2*N*X_max+1) for _ in range(N+1)]

for j in range(N+1):
    for t in range(2*N*X_max+1):
        if j == 0 and t == N*X_max:
            dp[j][t] = 1
        elif j >= 1 and ( t - X[j-1] < 0 or t - X[j-1] > 2*N*X_max):
            dp[j][t] = dp[j-1][t]
        elif j >= 1 and 0 <= t - X[j-1] <= 2*N*X_max:
            dp[j][t] = dp[j-1][t] + dp[j-1][t-X[j-1]]
      
print(dp[N])
print(dp[N][N*X_max] - 1)

""" 
# むずい。。。ギブアップ
https://atcoder.jp/contests/dp/tasks

# 動的計画法
https://qiita.com/drken/items/dc53c683d6de8aeacf5a

# 動的計画法パターン
https://wakabame.hatenablog.com/entry/2017/09/10/211428

 """