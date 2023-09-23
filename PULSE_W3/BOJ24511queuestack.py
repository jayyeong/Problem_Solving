import sys
from collections import deque

N = int(sys.stdin.readline())

A = [int(x) for x in sys.stdin.readline().split()]
# 0이 큐 , 1 이 스택
B = [int(x) for x in sys.stdin.readline().split()]

M = int(sys.stdin.readline())

C = deque([int(x) for x in sys.stdin.readline().split()])

answer = []
for i in range(len(B) - 1, -1, -1):
    if A[i] == 0:
        answer.append(B[i])
answer += C

print(' '.join(map(str,answer[:len(C)])))