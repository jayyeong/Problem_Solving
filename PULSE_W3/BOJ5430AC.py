from collections import deque

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    command_list = list(input())
    del command_list[-1]

    n = int(input())
    a = input().strip()

    if n != 0:
        deq = deque(map(int,a[1:-1].split(sep=',')))
    else:
        deq = deque()

    Reverseflag = False
    errorflag = False

    for command in command_list:
        if command == 'R':
            Reverseflag = not Reverseflag

        if command == 'D':
            if deq:
                if Reverseflag:
                    deq.pop()
                else:
                    deq.popleft()

            else:
                errorflag = True
                break
    if errorflag:
        print("error")
    else:
        if Reverseflag:
            deq.reverse()
        print("[%s]"%(','.join(map(str,deq))))