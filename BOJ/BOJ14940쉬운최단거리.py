from collections import deque

dx = [0, 1,  0, -1]
dy = [1, 0, -1, 0]
start_x, start_y = 0, 0
maze = []
wall_list = []
que = deque()

n, m = map(int, input().split())
visited = [[-1] * m for _ in range(n)]

for i in range(n):
    line = [int(x) for x in input().split()]
    for j in range(m):
        if line[j] == 2:
            start_x, start_y = i, j
        elif line[j] == 0:
            wall_list.append([i, j])
    maze.append(line)

visited[start_x][start_y] = 0

for pos in wall_list:
    visited[pos[0]][pos[1]] = 0

que.append([start_x, start_y])

while que:
    x, y = que.popleft()
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                que.append([nx, ny])

for i in range(n):
    print(" ".join(map(str, visited[i])))