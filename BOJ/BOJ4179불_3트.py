from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

R, C = map(int, input().rstrip().split())

maze = []
cutTime = 0
fireList = deque()
startPos = deque()

for i in range(R):
    maze.append(list(input().rstrip()))
    for j in range(C):
        if maze[i][j] == 'J':
            startPos.append((i, j, 0))

        elif maze[i][j] == 'F':
            fireList.append((i, j, 0))

while startPos:
    cutTime += 1

    while startPos and startPos[0][2] < cutTime:
        x, y, answer = startPos.popleft()

        if (x == 0 or x == R - 1 or y == 0 or y == C - 1) and maze[x][y] == 'J':
            print(answer + 1)
            exit()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if maze[nx][ny] == '.':
                    maze[nx][ny] = 'J'
                    startPos.append((nx, ny, answer + 1))

    while fireList and fireList[0][2] < cutTime:

        x, y, t = fireList.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if maze[nx][ny] == '.' or maze[nx][ny] == 'J':
                    maze[nx][ny] = 'F'
                    fireList.append((nx, ny, t + 1))

print("IMPOSSIBLE")