import sys

N, M = map(int, sys.stdin.readline().split())

chanho = [int(x) for x in sys.stdin.readline().split()]

half = N // 2
bad_count = 0

for i in range(N - 1):
    Sum = 0
    arr = [int(x) for x in sys.stdin.readline().split()]
    for j in range(M):
       Sum += abs(arr[j] - chanho[j])

    if Sum > 2000:
        bad_count += 1

if bad_count >= half:
    print('YES')
else:
    print('NO')