N = int(input())

arr = list(map(int, input().split()))

arr_count_0 = arr.count(0)
arr_count_1 = arr.count(1)

#Sum = arr_count_0 * arr_count_1 * 2  + (N - arr_count_1 - arr_count_0) * arr_count_0 + (arr_count_0 * (arr_count_0 - 1) // 2)

Sum = arr_count_0 * (arr_count_1 * 2  + N - arr_count_1 - arr_count_0 + ((arr_count_0 - 1) / 2))

print(int(Sum))

# 0 0 0 1 1 2 2 3
#
# 1 1 2 2 1 1 1  = 9
# 1 2 2 1 1 1  = 8
# 2 2 1 1 1  = 7

