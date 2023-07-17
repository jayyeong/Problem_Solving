import sys
MAXTIME = 1000001
N = int(input())

in_time = [0] * MAXTIME
out_time = [0] * MAXTIME
D = [0] * MAXTIME

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    in_time[a] += 1
    out_time[b] += 1

for i in range(1, MAXTIME):
    D[i] = D[i - 1] + in_time[i] - out_time[i - 1]

Q = int(sys.stdin.readline().rstrip())
Qlist = [int(x) for x in sys.stdin.readline().split()]

for q in Qlist:
    print(D[q])