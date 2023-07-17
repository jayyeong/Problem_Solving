T = int(input())

N, M = map(int, input().split())

manito = [[] for _ in range(N + 1)]

for _ in range(M):
    #manito.append([int(x) for x in input().split()])
    X, Y, C = map(int, input().split())
    manito[X].append([Y, C])

print(manito)
answer = 0
visited = [False] * (N + 1)


def dfs(ancestor, now, Sum):
    global answer


    if manito[now]:
        for next in manito[now]:
            if ancestor == next[0]:
                Sum += next[1]
                print(Sum)
                return

            dfs(ancestor, next[0], Sum + next[1])


for a in manito[1]:
    dfs(1, a[0], 0)



print(answer)