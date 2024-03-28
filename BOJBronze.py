word = list(input())

w = len(word)

for i in range(w//2):
    if word[i] != word[w - 1 - i]:
        print(0)
        exit()
print(1)