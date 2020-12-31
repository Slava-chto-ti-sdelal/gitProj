import numpy as np


class PrintAverage(Exception):
    pass


class PrintDispersion(Exception):
    pass


class PrintQuantity(Exception):
    pass


def coroutines():
    elem = []
    try:
        while True:
            try:
                a = yield
                elem.append(a)
            except PrintDispersion:
                yield np.var(elem)
            except PrintAverage:
                yield np.mean(elem)
            except PrintQuantity:
                yield len(elem)
    finally:
        print()


coroutine = coroutines()
next(coroutine)

for i in range(12):
    coroutine.send(i)
    if i % 2 == 0:
        print("Среднее:", coroutine.throw(PrintAverage))
        next(coroutine)
    if i % 3 == 0:
        print("Дисперсия:", coroutine.throw(PrintDispersion))
        next(coroutine)
    if i % 4 == 0:
        print("Количество:", coroutine.throw(PrintQuantity))
        next(coroutine)

coroutine.close()
