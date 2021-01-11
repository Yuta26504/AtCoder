N, A, B = map(int, input().split())

total = list()
for i in range(1, N+1):
    disit = list(map(int, str(i)))
    if A <= sum(disit) <= B:
        total.append(i)

print(sum(total))

""" 
# 正解
N, A, B = map(int, input().split())
print(sum(i for i in range(1, N+1) if A <= sum(map(int, str(i))) <= B))
 """