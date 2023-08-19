N = int(input())

INF = int(10e9)
DP = [INF] * (5001)

DP[3] = 1
DP[5] = 1

for i in range(6, N + 1):
        DP[i] = min(DP[i - 3], DP[i - 5]) + 1

if DP[N] < INF:
    print(DP[N])
else:
    print(-1)