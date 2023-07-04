from collections import deque

n = 0
result = 0

N, K = map(int, input().split())
answer = list(map(int, input().split()))
OMR = list(map(int, input().split()))

def pull(arr, p):
    a1, a2 = arr[:p], deque(arr[p:])
    a2.rotate(-1)
    a2[-1] = -1
    return a1 + list(a2)

def push(arr, p):
    a1, a2 = arr[:p], deque(arr[p:])
    a2.rotate(1)
    a2[0] = -1
    return a1 + list(a2)

def backTracking(n, Arr):
    global result
    count = 0

    for i in range(N):
        if answer[i] == Arr[i]:
            count += 1

    if count > result:
        result = count

    if n < K:
        for i in range(N):
            backTracking(n + 1, pull(Arr, i))
            backTracking(n + 1, push(Arr, i))

backTracking(0, OMR)
print(result)