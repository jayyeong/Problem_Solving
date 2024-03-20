from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
campus = [] # 캠퍼스 정보를 담는 리스트
ix, iy = 0, 0 # 최초 시작 위치의 좌표 ix, iy
answer = 0 # 만날 수 있는 사람의 수, 출력값

N, M = map(int, input().split()) # 캠퍼스 크기 입력

for i in range(N):
    campus.append(list(input()))
    for j in range(M):
        if campus[i][j] == 'I': # 시작 위치 찾기
            ix, iy = i, j

visited = [[0] * M for _ in range(N)] # 방문 정보를 담는 리스트

deq = deque()
deq.append([ix, iy]) # 최초 시작 위치 insert

while deq: # 큐가 빌 때까지
    x, y = deq.popleft()
    for i in range(4):  # 상하좌우 탐색
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0: # 방문 안했으면
            visited[nx][ny] = 1 # 방문 표시
            if campus[nx][ny] == 'O':  # 빈 공간 이면
                deq.append([nx, ny])
            elif campus[nx][ny] == 'P':  # 사람 이면
                deq.append([nx, ny])
                answer += 1 # 만난 사람 수 증가

print('TT' if answer == 0 else answer) # 정답 출력