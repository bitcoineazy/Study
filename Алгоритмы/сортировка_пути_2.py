x = 14
y = '0 3 41 0 0 0 0 0 49 0 0 56 0 88'.split(' ') # answer: 0 1 2 1 0
#x = int(input())
#y = input().split(' ')

def sort_alg(n, points):
    points = [int(x) for x in points]
    zero_indexes = []
    for i in points:
        if i == 0:
            zero_indexes.append(points.index(i))
            break
    for i in reversed(points):
        if i == 0:
            zero_indexes.append((len(points) - points.index(i)) - 1)
            break
    print(zero_indexes)
    output = []
    for i in range(n):
        output.append(0)
    for i in range(zero_indexes[0], len(output)):
        if points[i] == 0:
            output[i] = 0
        else:
            output[i] = output[i-1] + 1
    print(points)
    for i in range(zero_indexes[1], zero_indexes[0], -1):
        if points[i] == 0:
            output[i] = 0
        else:
            output[i] = min(output[i], output[i+1] + 1)
    for i in range(zero_indexes[0], -1, -1):
        if points[i] == 0:
            output[i] = 0
        else:
            output[i] = output[i+1] + 1
    print(' '.join(str(x) for x in output))

sort_alg(x, y)
