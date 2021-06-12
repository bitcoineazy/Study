expression = {2: 4, 3: 2, 12: 6, 5: 4, 1: 3}
print([x + y for x, y in expression.items() if (x + y) % 2 == 0])


def psort(**kwargs):
    values = [y for x, y in kwargs.items()]
    res = []
    for i in sorted(values):
        for x, y in kwargs.items():
            if y == i:
                res.append(x)
    print(res)


psort(c=21, g=33, h=55, j=2)
