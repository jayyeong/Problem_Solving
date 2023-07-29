import sys

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
#print(parent)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a

for _ in range(m):
    k, A, B = map(int, sys.stdin.readline().rstrip().split())

    if k == 0:
        union(A, B)

    elif k == 1:
        if find(A) == find(B):
            print('YES')
        else:
            print('NO')

    #print(parent)