from collections import Counter

x = int(input())
y = [x for x in range(4) for x in input()]

def algo(k, area):
    c = Counter(int(x) for x in area if x != '.')
    print(c.values())
    attempts = k * 2
    result = 0
    solved = sorted([int(x) for x in c.values()])
    print(solved)
    for i in range(min(solved)):
        print(i)
        if attempts >= i:
            attempts -= i
            result += 1

    print(result)


algo(x, y)
