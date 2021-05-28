x = 20
y = '3 15 0 22 31 32 0 41 0 0 50 0 0 66 0 76 77 82 0 89'.split(' ') # answer: 0 1 2 1 0
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
            zero_indexes.append((len(points) - points.index(i)) - 2)
            break
    #print(zero_indexes)
    output = []
    for i in range(n):
        output.append(0)
    for i in range(zero_indexes[0], n):
        if points[i] == 0:
            output[i] = 0
        else:
            output[i] = output[i-1] + 1
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
