N, M = map(int, input().split())

numList = [int(x) for x in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())

    i -= 1
    j -= 1

    for k in range((j - i + 1)//2):
        tmp = numList[i + k]
        numList[i + k] = numList[j - k]
        numList[j - k] = tmp

print(' '.join(map(str, numList)))