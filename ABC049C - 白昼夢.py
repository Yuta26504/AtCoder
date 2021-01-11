""" import itertools
S = input()
s = S
T = ["dream", "dreamer", "erase", "eraser"]

for i in list(itertools.combinations(T, 2)):
    for n in i:
        S = S.replace(n, "")
    if len(S) == 0:
        print("YES")
        exit()
    S = s

print("NO") """

import re
S = input()
print("YES" if re.match("^(dream|dreamer|erase|eraser)+$", S) else "NO")


#　WA
""" 
import re
S = input()
print("YES" if re.match("^(dream|dreamer|erase|eraser)+$", S) else "NO")
# re.match の + は直前のパターンを一回以上繰り返すという意味
# ^　は先頭、$ は末尾
 """