import sys

INF = int(1e9)
N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append([int(x) for x in sys.stdin.readline().split()])

box = [[0] * M for _ in range(N)]

box[0] = arr[0]

for i in range(N - 1):

    for j in range(M):

        temp = INF

        for k in range(M):
            if box[i][k] <= temp and j != k:
                temp = box[i][k]

        box[i + 1][j] = arr[i + 1][j] + temp

print(min(box[N - 1]))