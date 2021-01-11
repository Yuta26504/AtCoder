S = list(input())

s = ""
for i in S:
    if i == "B":
        if len(s) != 0:
            s = s[:-1]
        else:
            pass
    else:
        s += i
print(s)

