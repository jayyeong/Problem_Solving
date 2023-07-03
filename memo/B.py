import sys
from itertools import combinations

INF = 10**9 + 1

N, K, M = map(int, input().split())

arr = [int(x) for x in input().split()]

graph = [[INF] * (N) for _ in range(N)]

print(arr)

factory = [[] for _ in range(K)]
print(factory)
for i in range(N):
    factory[arr[i] - 1].append(i)

print(factory)

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())

    if graph[a - 1][b - 1] == INF:
        graph[a - 1][b - 1] = c
        graph[b - 1][a - 1] = c

    elif graph[a - 1][b - 1] < c:
        graph[a - 1][b - 1] = c
        graph[b - 1][a - 1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in graph:
    print(i)

