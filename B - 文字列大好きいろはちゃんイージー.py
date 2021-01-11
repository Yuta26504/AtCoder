N, L = map(int, input().split())

S = [input() for _ in range(N)]
S = "".join(sorted(S))

print(S)


