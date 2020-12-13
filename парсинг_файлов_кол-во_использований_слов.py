def exercise4():
    import matplotlib.pyplot as plt
    import re

    pa = re.compile('\w+')

    def work_harder():
        dicty = {}
        with open('voyna-i-mir-tom-1.txt', mode='r') as fi:
            f1 = str(fi.read().strip())
            x1 = pa.findall(f1)
            x2 = x1[0:100]
            for i in x2:
                if len(i) >= 4:
                    dicty[i] = x1.count(i)
            d3 = dict(sorted(dicty.items(), key=lambda x: x[1], reverse=True))
        return d3
    xs = work_harder()
    xs1 = {}
    c = 0
    for i, j in xs.items():
        xs1[i] = j
        c += 1
        if c == 10:
            break
    fig, ax = plt.subplots()
    ax.bar(xs1.keys(), xs1.values())
    ax.set_facecolor('white')
    fig.set_facecolor('white')
    fig.set_figwidth(12)
    fig.set_figheight(6)
    plt.show()

exercise4()