N = int(input())

fruit_list = { 'STRAWBERRY': 0, 'BANANA' : 0 , 'LIME' : 0 , 'PLUM' : 0}
for i in range(N):
    S, X = input().split()
    fruit_list[S] += int(X)

print('YES' if list(fruit_list.values()).count(5) else 'NO')