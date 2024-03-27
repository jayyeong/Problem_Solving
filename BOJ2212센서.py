diffList = [] # 각 센서의 거리 차이 저장

N = int(input())
K = int(input())

sensorList = [int(x) for x in input().split()]

if K >= N:
    print(0)
    exit()

sensorList.sort() # 센서 위치 정렬

for i in range(1, N):
    diffList.append(sensorList[i] - sensorList[i - 1])

for _ in range(K - 1):
    diffList[diffList.index(max(diffList))] = 0

print(sum(diffList))