N = int(input())
cards = list(map(int, input().split()))
Alice = []
Bob = []

flag = True
while len(cards) > 0:
    if flag == True:
        Alice.append(cards.pop(cards.index(max(cards))))
        flag =False
    else:
        Bob.append(cards.pop(cards.index(max(cards))))
        flag = True

print(sum(Alice) - sum(Bob))

""" 
# 正解　ソートしてから
N = int(input())
a = sorted(map(int, input().split()))[::-1]
print(sum(a[::2])-sum(a[1::2]))
 """
