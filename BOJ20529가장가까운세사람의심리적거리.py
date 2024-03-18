MBTI1 = ['E', 'I']
MBTI2 = ['N', 'S']
MBTI3 = ['T', 'F']
MBTI4 = ['J', 'P']

MBTI_TEST = [['E', 'I'], ['N', 'S'], ['T', 'F'], ['J', 'P']]
T = int(input())

for _ in range(T):
    N = int(input())
    mbti_list = [x for x in input().split()]

    answer = -1

    case = ''

    for p in MBTI_TEST[0]:
        for q in MBTI_TEST[1]:
            for r in MBTI_TEST[2]:
                for s in MBTI_TEST[3]:
                    case = p + q + r + s
                    count = 0
                    for mbti in mbti_list:
                        if mbti == case:
                            count += 1
                    if count >= 3:
                        answer = 0

    if answer == 0:
        print(answer)
        continue

    for i in [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]:
        for q in MBTI_TEST[i[0]]:
            for r in MBTI_TEST[i[1]]:
                for s in MBTI_TEST[i[2]]:
                    count = 0
                    for mbti in mbti_list:
                        if mbti[i[0]] == q and mbti[i[1]] == r and mbti[i[2]] == s:
                            count += 1
                    if count >= 3:
                        answer = 2

    if answer == 2:
        print(answer)
        continue

    for i in [[0,1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]:
        for p in MBTI_TEST[i[0]]:
            for q in MBTI_TEST[i[1]]:
                count = 0
                for mbti in mbti_list:
                    if mbti[i[0]] == p and mbti[i[1]] == q:
                        count += 1
                if count >= 3:
                    answer = 4

    if answer == 4:
        print(answer)
        continue

    for i in range(4):
        for p in MBTI_TEST[i]:
            count = 0
            for mbti in mbti_list:
                if mbti[i] == p:
                    count += 1
            if count >= 3:
                answer = 6

    if answer == 6:
        print(answer)
        continue

    if answer == -1:
        print(8)
        continue