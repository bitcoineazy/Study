import matplotlib.pyplot as plt
import numpy as np
from numpy import exp, sqrt
from itertools import permutations


def polnper(towns):
    a = list(permutations(list(range(len(towns[0])))[1:]))
    s = []
    for i in a:
        s.append([0] + list(i) + [0])
    summ = -1
    path = []
    for i in s:
        sm = 0
        for a in range(len(i) - 1):
            sm += towns[i[a]][i[a + 1]]
        if sm < summ or summ == -1:
            path = i
            summ = sm
    path1 = path.copy()
    for i in range(len(path)):
        path[i] += 1
    return path1, path, summ


def conv(var=None, X=None, Y=None, n=None):
    if type(var) == np.ndarray:
        ls = []
        for i in range(n):
            s = []
            for j in range(n):
                s.append(var[i, j])
            ls.append(s)
        return ls
    elif type(var) == list:
        x = [X[int(i)] for i in var]
        y = [Y[int(i)] for i in var]
        return x, y


def cvx(X, Y, n):
    for ib in np.arange(0, n, 1):
        M = np.zeros([n, n])
        for i in np.arange(0, n, 1):
            for j in np.arange(0, n, 1):
                if i != j:
                    M[i, j] = sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
                else:
                    M[i, j] = 0
    m = []
    for i in range(n):
        s = []
        for j in range(n):
            s.append(int(M[i, j]))
        m.append(s)
    return m


n = 50;
m = 100;
way = [];
a = 0
X = np.random.uniform(a, m, n)
Y = np.random.uniform(a, m, n)
X = [10, 5, 20, 30, 30, 20, 20, 50, 50, 85, 85, 75, 35, 25, 30, 47, 50]
Y = [10, 65, 120, 90, 50, 55, 50, 75, 25, 50, 110, 80, 25, 70, 10, 50, 100]
n = len(X)
RS = [];
RW = [];
RIB = []
s = []
massiv = cvx(X[:5], Y[:5], 5)
print(massiv)
for ib in np.arange(0, n, 1):
    M = np.zeros([n, n])
    for i in np.arange(0, n, 1):
        for j in np.arange(0, n, 1):
            if i != j:
                M[i, j] = sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
            else:
                M[i, j] = float('inf')

    way = []
    way.append(ib)
    for i in np.arange(1, n, 1):
        s = []
        for j in np.arange(0, n, 1):
            s.append(M[way[i - 1], j])
        way.append(s.index(min(s)))
        for j in np.arange(0, i, 1):
            M[way[i], way[j]] = float('inf')
            M[way[i], way[j]] = float('inf')
    S = sum([sqrt((X[way[i]] - X[way[i + 1]]) ** 2 + (Y[way[i]] - Y[way[i + 1]]) ** 2) for i in
             np.arange(0, n - 1, 1)]) + sqrt((X[way[n - 1]] - X[way[0]]) ** 2 + (Y[way[n - 1]] - Y[way[0]]) ** 2)
    RS.append(S)
    RW.append(way)
    RIB.append(ib)

S = min(RS)
way = RW[RS.index(min(RS))]
ib = RIB[RS.index(min(RS))]
X1 = [X[way[i]] for i in np.arange(0, n, 1)]
Y1 = [Y[way[i]] for i in np.arange(0, n, 1)]

(a, b, c) = polnper(massiv)
print(a, b, c)

plt.title('Общий путь-%s.Номер города-%i.Всего городов -%i.\n Координаты X,Y заданы' % (round(S, 3), ib, n), size=14)
plt.plot(X1, Y1, color='r', linestyle=' ', marker='o')
plt.plot(X1, Y1, color='b', linewidth=1)
X2 = [X[way[n - 1]], X[way[0]]]
Y2 = [Y[way[n - 1]], Y[way[0]]]
plt.plot(X2, Y2, color='g', linewidth=2, linestyle='-', label='Путь от  последнего \n к первому городу')
plt.legend(loc='best')
plt.grid(True)
plt.show()
(x1, y1) = conv(a, X[:5], Y[:5])
plt.title("Полнывй перебор")
plt.plot(x1, y1)
plt.plot(x1, y1, color='r', linestyle=' ', marker='o')
plt.grid(True)
plt.show()
