from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

R, C = map(int, input().split())

maze = []
answer = 0
deq = deque()

for i in range(R):
    maze.append(list(input()))
    for j in range(C):
        if maze[i][j] == 'J':
            deq.append((i, j, 'J'))
            maze[i][j] = 1

for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':
            deq.append((i, j, 'F'))
            maze[i][j] = '#'

while deq:
    x, y, value = deq.popleft()

    if (x == 0 or x == R - 1 or y == 0 or y == C - 1) and value == 'J':
        if maze[x][y] != '#':
            print(maze[x][y])
            exit()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if value == 'J' and maze[x][y] != '#':
                if maze[nx][ny] == '.':
                    deq.append((nx, ny, 'J'))
                    maze[nx][ny] = maze[x][y] + 1

            elif value == 'F':
                maze[x][y] = '#'
                if maze[nx][ny] != '#':
                    deq.append((nx, ny, 'F'))
                    maze[nx][ny] = '#'

    #print(maze)

print("IMPOSSIBLE")