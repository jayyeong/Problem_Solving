
degree = 0

for i in range(10):
    t = int(input())

    if t == 1:
        degree += 90

    elif t == 2:
        degree += 180

    elif t == 3:
        degree -= 90

    degree %= 360

if degree == 0:
    print('N')
elif degree == 90:
    print('E')
elif degree == 180:
    print('S')
elif degree == 270:
    print('W')
