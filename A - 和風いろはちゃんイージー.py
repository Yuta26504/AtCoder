N = list(map(int, input().split()))

if N.count(5) == 2 and N.count(7) == 1:
    print("YES")
else:
    print("NO")