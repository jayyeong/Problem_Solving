import sys

#INF = int(1e9)
N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append([int(x) for x in sys.stdin.readline().split()])

for i in range(N - 1):

    for j in range(M):

        #temp = INF

        #for k in range(M):
        #    if arr[i][k] <= temp and j != k:
        #        temp = arr[i][k]

        temp = min(arr[i][:j] + arr[i][j + 1:])

        arr[i + 1][j] += temp

print(min(arr[N - 1]))