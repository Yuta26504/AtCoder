import collections

w = list(input())
count = collections.Counter(w)

def check(values):
    for i in values:
        if i % 2 != 0:
            return "No"
    return "Yes"
print(check(count.values()))