N, K = map(int, input().split())
D = list(map(int, input().split()))

like = []
for i in range(10):
    if i not in D:
        like.append(i)
pay = []
flag = True
for n in str(N):
    for i in sorted(like):
        if int(n) < i and flag == True:
            pay.append(i)
            flag = False
            break
        elif int(n) <= i:
            pay.append(i)
            break
        elif int(n) >= i and flag == False:
            pay.append(i)
            break


if len(pay) == 0:
    pay.append(min(like))
total = int("".join(map(str, pay)))

if total < N:
    while total < N:
        pay.append(min(like))
        total = int("".join(map(str, pay)))
print(total)

""" 
# 一つずつ足して嫌いな文字が入ってないか確認
N, K = map(int, input().split())
D = list(map(str, input().split()))
x = N-1
while True:
    x += 1
    s = str(x)
    if not any((c in s) for c in D):
        print(x)
        exit(0)
 """