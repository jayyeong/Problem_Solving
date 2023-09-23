from collections import deque

N = int(input())

A = deque([int(x) for x in input().split()])
B = deque()


answer = []
count = 0

for i in range(N, 0, -1):
    if i in A:
        a = A.pop()
        count += 1
        while a != i:
            B.append(a)
            answer.append([1, 2])
            a = A.pop()
            count += 1
        answer.append([1, 3])

    elif i in B:
        b = B.pop()
        count += 1
        while b != i:
            A.append(b)
            answer.append([2, 1])
            b = B.pop()
            count += 1
        answer.append([2, 3])

print(count)
for ans in answer:
    print(' '.join(map(str, ans)))
