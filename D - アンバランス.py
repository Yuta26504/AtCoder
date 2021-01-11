S = list(input())

def search(S):
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            return i+1, i+2
    for i in range(len(S)-2):
        if S[i] == S[i+2]:
            return i+1, i+3
    return -1, -1

print(*search(S))
