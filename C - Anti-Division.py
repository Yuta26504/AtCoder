A, B, C, D = map(int, input().split())

total = 0
for i in range(A, B+1):
    if i % C != 0 and i % D != 0:
        total += 1
print(total)

# 計算時間たりない
""" 
# 正解
import math
a,b,c,d=map(int,input().split())
f=c*d//math.gcd(c,d)
print(b-a+1 - (b//c-(a-1)//c) - (b//d-(a-1)//d) + (b//f-(a-1)//f))
 """