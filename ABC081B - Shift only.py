N = int(input())
A = list(map(int, input().split()))

def harf(A):
    for i in A[-N:]:
        if i%2 == 0:
            A.append(i//2)
        else:
            pass

sum = 0
while len(A) == N:
    harf(A)
    del A[0:N]
    if len(A) == N:
        sum += 1

print(sum)

""" 
# 正解
N = int(input())
A = list(map(int, input().split()))
count = 0
while all(a % 2 == 0 for a in A):
    A = [a/2 for a in A]
    count += 1
print(count)
 """