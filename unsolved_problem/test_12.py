
T = int(input())
N, M = map(int, input().split())
weight = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    X, Y, C = map(int, input().split())
    weight[X][Y] = C

def find_cycles(graph):
    visited = set()  # 방문한 노드를 저장하기 위한 집합
    cycles = []  # 발견된 사이클을 저장하기 위한 리스트

    for node in graph:
        if node not in visited:
            path = [node]  # 경로를 리스트로 변경하여 저장
            dfs(node, graph, visited, cycles, path)

    return cycles


def dfs(node, graph, visited, cycles, path):
    visited.add(node)  # 현재 노드를 방문했음을 표시

    for neighbor in graph[node]:
        if neighbor in path:  # 현재 경로에 이미 있는 노드라면 사이클 발견
            cycles.append(path + [neighbor])  # 사이클을 발견하면 경로를 사이클 리스트에 추가
        elif neighbor not in visited:
            dfs(neighbor, graph, visited, cycles, path + [neighbor])

    visited.remove(node)  # DFS가 끝나면 현재 노드를 방문한 집합에서 제거

# 그래프 예시
# 그래프 예시
graph = {
    '1': ['1'],
    '2': ['3'],
    '3': ['2']
}


# 모든 사이클 찾기
cycles = find_cycles(graph)

for cycle in cycles:
    if cycle[0] == cycle[-1]:
        Sum = 0
        for i in range(len(cycle) - 1):
            Sum += weight[int(cycle[i])][int(cycle[i + 1])]
        print(Sum)