def f1(values: list[int]):
    return sum(x ** 2 for x in values if x % 2 == 0)

def f2(values: list[int]):
    return sum(x ^ 2 for i, x in enumerate(values) if i % 2 == 0)

def f3(values: list[int]):
    return sum(x * x if x % 2 == 0 else 0 for x in values)

def f4(values: list[int]):
    return sum(x ^ 2 for x in values[::2])

def f5(values: list[int]):
    pass
    #return sum(x ** 2 if x % 2 == 0 for x in values)

print(f1([2,3,4,5,6]))
print(f2([2,3,4,5,6])) #x
print(f3([2,3,4,5,6]))
print(f4([2,3,4,5,6]))
print(f5([2,3,4,5,6]))

print(1 + 2.3)
print(True == 1)