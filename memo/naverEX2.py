a_dic = {'BOOL':1, 'SHORT':2, 'FLOAT':4, 'INT':8, 'LONG':16}

tc1 = ["INT", "INT", "BOOL", "SHORT", "LONG"]
tc2 = ["INT", "SHORT", "FLOAT", "INT","BOOL"]
tc3 = ["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"]
tc4 = ["BOOL", "LONG", "SHORT", "LONG", "BOOL", "LONG", "BOOL", "LONG", "SHORT", "LONG", "LONG"]

answer = []

def solution(arr):
    last_ele = arr[0]
    word = '#' * a_dic.get(last_ele)

    for i in range(1, len(arr)):

        if arr[i] == 'BOOL':
            word += '#'

        elif arr[i] == 'SHORT':

            if len(word) % 2 != 0:
                while (len(word) % 2 != 0):
                    word += '*'

            word += '##'

        elif arr[i] == 'FLOAT':
            if len(word) % 4 != 0:
                while (len(word) % 4 != 0):
                    word += '*'

            word += '####'

        elif arr[i] == 'INT':
            if len(word) % 8 != 0:
                while(len(word) != 8):
                    word += '*'

            word += '########'

        elif arr[i] == 'LONG':
            if len(word) % 8 != 0:
                while(len(word) != 8):
                    word += '*'

            word += '#' * 16

        last_ele = arr[i]

        if len(word) >= 8:

            while(len(word) >= 8):
                answer.append(word[:8])
                word = word[8:]

    if len(word) % 8 != 0:
        while (len(word) != 8):
            word += '*'
        answer.append(word[:8])
        word = word[8:]

    print(len(answer))

    if len(answer) > 16:
        print('HALT')
        return

    print(answer)
    print(','.join(map(str,answer)))

tt = ['BOOL', 'SHORT', 'BOOL', 'SHORT','FLOAT','BOOL','BOOL','BOOL','SHORT','INT']

solution(tt)