import io
import sys

_INPUT = """\
6
1 1
2 2
3 3
4 4
5 5
6 6

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

flag = 0
for i in D:
    if flag < 3:
        if i[0]==i[1]:
            flag += 1
        else:
            flag = 0
    else:
        break
if flag == 3:
    print("Yes")
else:
    print("No")

    
