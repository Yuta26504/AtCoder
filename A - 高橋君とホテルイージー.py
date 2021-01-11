N, K, X, Y = (int(input()) for _ in range(4))

print(K*X + Y*(N-K) if N >= K else X*N)
