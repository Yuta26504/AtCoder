import io
import sys

_INPUT = """\
11

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------
N = input()
total = sum(list(map(int, N)))

count = 0
sup = []
for i in N:
    sup.append(int(i) % 3)
if total % 3 == 0:
    count += 0
elif len(N) == 1:
    count -= 1
elif total % 3 == 1:
    if 1 in sup:
        count += 1
    elif 0 in sup or 2 in sup:
        if len(N) == 2:
            count -= 1
        else:
            count +=2
elif total % 3 == 2:
    if 2 in sup:
        count += 1
    elif 0 in sup or 1 in sup:
        if len(N) == 2:
            count -= 1
        else:
            count +=2
    
print(count)


