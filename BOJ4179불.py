from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

R, C = map(int, input().split())

maze = []
answer = 0
fireList = deque()
startPos = deque()

for i in range(R):
    maze.append(list(input()))
    for j in range(C):
        if maze[i][j] == 'J':
            startPos.append((i, j, 0))

        elif maze[i][j] == 'F':
            fireList.append((i, j))

while startPos:

    while startPos:
        x, y, t = startPos.popleft()


        if (x == 0 or x == R - 1 or y == 0 or y == C - 1) and maze[x][y] == 'J':
            print(answer + 1)
            exit()

        maze[x][y] = '#'

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if maze[nx][ny] == '.':
                    maze[nx][ny] = 'J'

    answer += 1

    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'J':
                startPos.append((i, j, answer))

    while fireList:

        fx, fy = fireList.popleft()
        maze[fx][fy] = '#'

        for i in range(4):
            nfx, nfy = fx + dx[i], fy + dy[i]
            if 0 <= nfx < R and 0 <= nfy < C:
                if maze[nfx][nfy] == '.' or maze[nfx][nfy] == 'J':
                    maze[nfx][nfy] = 'F'

    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'F':
                fireList.append((i, j))

print("IMPOSSIBLE")