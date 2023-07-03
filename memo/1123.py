import collections

def calculate_delivery_limit(N, K, M, warehouses, roads):
    # 그래프 초기화
    graph = [[] for _ in range(N+1)]

    # 그래프 생성
    for road in roads:
        warehouse1, warehouse2, limit = road
        graph[warehouse1].append((warehouse2, limit))
        graph[warehouse2].append((warehouse1, limit))

    def bfs(start):
        queue = collections.deque([(start, float('inf'))])
        visited = [False] * (N+1)
        visited[start] = True
        max_limit = 0

        while queue:
            current, limit = queue.popleft()
            max_limit = max(max_limit, limit)

            for neighbor, neighbor_limit in graph[current]:
                if not visited[neighbor] and neighbor_limit >= limit:
                    visited[neighbor] = True
                    queue.append((neighbor, limit))

        return max_limit

    # 각 회사의 물류창고들의 배송 상한선 총합 계산
    company_delivery_limits = [0] * (K+1)
    for company, warehouses_list in warehouses.items():
        max_limit = 0
        for warehouse in warehouses_list:
            limit = bfs(warehouse)
            max_limit = max(max_limit, limit)
        company_delivery_limits[company] = max_limit

    return company_delivery_limits

# 입력 예시
N = 6  # 물류창고 개수
K = 3  # 회사