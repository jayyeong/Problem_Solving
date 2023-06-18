arr = list(map(int, input().split()))
answer = []
dic = {}

for i in range(len(arr)):
    if arr[i] not in dic.keys():
        dic[arr[i]] = 1
    else:
        dic[arr[i]] += 1

for d in dic:
    if dic.get(d) >= 2:
        answer.append(dic.get(d))

if answer:
    print(answer)
else:
    print([-1])