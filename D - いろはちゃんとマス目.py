mod = pow(10, 9) + 7 # 構造体(modint)
N = pow(10, 6)
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

H, W, A, B = map(int, input().split())

def comb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n-r)
    return fact[n] * factinv[r] * factinv[n-r] % mod

for i in range(2, N+1):
    fact.append((fact[-1]*i) % mod)
    inv.append((-inv[mod%i]*(mod//i)%mod))
    factinv.append((factinv[-1] * inv[-1]) % mod)
    
def convert(W, H):
    stage = W+(H-1)
    turn = W
    return stage, turn

first = []
second = []
for _ in range(W-B):
    first_num = convert(W, H-A)
    first.append(comb(first_num[0]-1, first_num[1]-1, mod))
    second_num = convert(W-B, A)
    second.append(comb(second_num[0]-1, second_num[1]-1, mod))
    W -= 1

sum = 0
for i, n in zip(first, second[::-1]):
    sum += i*n

print(sum%mod)

""" 
# 計算量間違い
first_stage = []
for i in range(W):
    first_stage.append(1)

second_stage = []
for i in range(W-B):
    second_stage.append(1)

def create_stage(stage):
    new_stage = []
    start = 0
    for i in stage:
        start += i%mod
        new_stage.append(start)
    return new_stage

def create_table(N, first_stage):
    table = []
    table.append(first_stage)
    flag = True
    for _ in range(N):
        if flag == True:
            table.append(create_stage(first_stage))
            flag = False
        else:
            table.append(create_stage(table[-1]))
    return table[-1]

table = create_table(H-A-1, first_stage)
second_table = create_table(A-1, second_stage)

sum = 0
for i, n in zip(table[B:], sorted(second_table, reverse=True)):
    sum += i*n

print(sum)
 """
""" 
# パスカルの三角形
https://www.wikiwand.com/ja/%E3%83%91%E3%82%B9%E3%82%AB%E3%83%AB%E3%81%AE%E4%B8%89%E8%A7%92%E5%BD%A2 

# 二項係数 nCr を高速計算
https://satoooh.com/entry/5195/
"""