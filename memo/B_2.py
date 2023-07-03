import sys
from itertools import combinations

v, k, e = map(int, input().split())
arr = [int(x) for x in input().split()]

factory = [[] for _ in range(k)]

for i in range(v):
    factory[arr[i] - 1].append(i + 1)

linelist = []

# 부모 테이블 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

# find 연산
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 간선 정보 담을 리스트와 최소 신장 트리 계산 변수 정의
edges = []
total_cost = 0

# 간선 정보 주어지고 비용을 기준으로 정렬
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선 정보 비용 기준으로 오름차순 정렬
edges.sort(reverse = True)

# 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
for i in range(e):
    cost, a, b = edges[i]
    # find 연산 후, 부모노드 다르면 사이클 발생 X으므로 union 연산 수행 -> 최소 신장 트리에 포함!
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        linelist.append([a, b, cost])
        total_cost += cost

#print(linelist)

INF = 10**9 + 1
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for e in linelist:
    graph[e[0]][e[1]] = e[2]
    graph[e[1]][e[0]] = e[2]

for k in range(v + 1):
    for i in range(v + 1):
        for j in range(v + 1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = min(graph[i][k],graph[k][j])

#print(factory)
for f in factory:
    sum = 0
    for a in combinations(f, 2):
        sum += graph[a[0]][a[1]]

    print(sum)


#print(total_cost)

