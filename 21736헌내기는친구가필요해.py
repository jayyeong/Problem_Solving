from collections import deque

N, M = map(int, input().split())

campus = []
ix, iy = 0, 0

for i in range(N):
    campus.append(list(input()))
    for j in range(M):
        if campus[i][j] == 'I':
            ix, iy = i, j

# print(ix, iy)
# print(campus)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

deq = deque()
deq.append([ix, iy])
answer = 0

visited = [[0] * M for _ in range(N)]

# print(visited)

while deq:
    x, y = deq.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            if campus[nx][ny] == 'O':
                deq.append([nx, ny])
            elif campus[nx][ny] == 'P':
                deq.append([nx, ny])
                answer += 1

if answer == 0:
    print('TT')
else:
    print(answer)