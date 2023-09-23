a = [1, 2, 3, 4, 5]
b = [0, 1, 2, 3, 4]

# print(a[:-1] == b[1:])

part_one = [int(x) for x in list(input())]
part_two = [int(x) for x in list(input())]

l1 = len(part_one)
l2 = len(part_two)

answer = l1 + l2

flag = False

for i in range(l1):
    for j in range(l2):
        if part_two[j] == 2 and part_one[j + i] == 2:
            flag = False
            break
        else:
            flag = True
            #print(j, j + i)

        if i + j == l1 - 1:
            flag = True
            break

    if flag == True:
        temp = max(i + l2, l1)
        answer = min(answer, temp)
        break

for i in range(l2):
    for j in range(l1):
        if part_two[i + j] == 2 and part_one[j] == 2:
            flag = False
            break
        else:
            flag = True

        if i + j == l2 - 1:
            flag = True
            break

    if flag == True:
        temp = max(i + l1, l2)
        answer = min(answer, temp)
        break

print(answer)