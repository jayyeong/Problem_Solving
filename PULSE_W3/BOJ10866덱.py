from collections import deque
import sys
N = int(input())

arr = deque()

for i in range(N):
    words = sys.stdin.readline().rstrip().split()

    if words[0] == 'push_front':
        arr.appendleft(int(words[1]))
    elif words[0] == 'push_back':
        arr.append(int(words[1]))
    elif words[0] == 'pop_front':
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif words[0] == 'pop_back':
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif words[0] == 'size':
        print(len(arr))
    elif words[0] == 'empty':
        if not arr:
            print(1)
        else:
            print(0)
    elif words[0] == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif words[0] == 'back':
        if arr:
            print(arr[-1])
        else:
            print(-1)