def fill1(temperatures: list[float | None]):
    total, count = 0, 0
    for t in temperatures:
        if t is not None:
            total += t
            count += 1
    avg = total / count
    for t in temperatures:
        if t is None:
            t = avg
    return temperatures

def fill2(temperatures: list[float | None]):
    avg = sum(temperatures) / len(temperatures)
    for i in range(len(temperatures)):
        if temperatures[i] is None:
            temperatures[i] = avg
    return temperatures

def fill3(temperatures: list[float | None]) -> None:
    good = [t for t in temperatures if t]
    avg = sum(good) / len(good)
    for i, t in enumerate(temperatures):
        temperatures[i] = t or avg
    print(temperatures)

def fill4(temperatures: list[float | None]) -> None:
    good = [t for t in temperatures if t is not None]
    avg = sum(good) / len(good)
    temperatures = [t or avg for t in temperatures]
    print(temperatures)

def fill5(temperatures: list[float | None]) -> None:
    good = [t for t in temperatures if t is not None]
    avg = sum(good) / len(good)
    temperatures[:] = [t if t is not None else avg for t in temperatures]
    print(temperatures)

tem1 = [2, None, 3, None, 4]
tem2 = [1, None, 3, None, 5]
tem3 = [2, None, 3, None, 4]
tem4 = [1, None, 3, None, 5]
tem5 = [7, None, 7, None, 7]

temA = [None, -1, 0]
print(fill1(temA))

#fill3(temA)
fill4(temA)
fill5(temA)
