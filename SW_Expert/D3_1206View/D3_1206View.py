for t in range(1, 11):
    N = int(input())

    buildings = [int(x) for x in input().split()]

    Sum = 0
    for i in range(2, N - 2):
        ans = buildings[i] - max(buildings[i - 2:i] + buildings[i + 1: i + 3])
        if(ans < 0):
            ans = 0
        Sum += ans

    print('#', end = '')
    print(t, Sum)