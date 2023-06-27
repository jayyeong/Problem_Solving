desktop = ['+---+', '+des+', '+---+']
display = ['+---+', '+   +', '+dis+', '+   +','+---+']
memory = ['+mem+']
sp = '     '
arr = [['des', 'dis', 'mem'], [], []]

ans = []
count = 0

N = int(input())

def hanoi(n, from_pos, to_pos, aux_pos):
    global arr
    if n == 1:
        print(from_pos, to_pos)
        arr[to_pos].append(arr[from_pos].pop(-1))
        print(arr)
        return

    hanoi(n - 1, from_pos, aux_pos, to_pos)

    hanoi(1, from_pos, to_pos, aux_pos)

    hanoi(n - 1, aux_pos, to_pos, from_pos)

hanoi(3, 0, 2, 1)