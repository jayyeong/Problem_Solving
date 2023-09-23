N = int(input())

for i in range(1, N + 1):
    words = input().split()
    words.reverse()
    #print(words)

    answer = 'Case #' + str(i) +': ' + " ".join(words)
    print(answer)
