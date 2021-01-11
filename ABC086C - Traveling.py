N = int(input())
t0 ,x0, y0 = 0, 0, 0

flag = True
for _ in range(N):
    t, x, y = map(int, input().split())
    distance = abs(x - x0) + abs(y - y0)
    time = abs(t - t0)
    t0 ,x0, y0 = t, x, y

    if distance > time and distance % 2 != time % 2:
        flag =False

if flag == True:
    print("Yes")
else:
    print("No")

# 時間が偶数の時、距離も偶数でなければ戻れない
