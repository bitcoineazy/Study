from collections import Counter


def algo(k, area):
    counter = Counter(int(x) for x in area if x != '.')
    attempts = k * 2
    return sum(x <= attempts for x in counter.values())


if __name__ == '__main__':
    x = int(input())
    y = [x for x in range(4) for x in input()]
    print(algo(x, y))
