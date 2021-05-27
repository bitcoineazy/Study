x = 5
y = '0 1 4 9 5 0'.split(' ') # answer: 0 1 2 1 0

def alg(n, points):
    counter = 0
    ranges = []
    zero_indexes = []
    popped = []
    for i in points:
        if i == '0':
            zero_indexes.append(points.index(i))


    length = 0
    print(points)
    for i in points:
        if int(i) == 0:
            ranges.append(counter)
            counter = 0
        else:
            counter += 1
            #ranges.append(counter)
    st = []
    c = 0
    for i in range(len(ranges) - 1):
        range_fill = ranges[i+1] - ranges[i]
        if range_fill % 2:
            st.append(0)
            for i in range((range_fill // 2) + 1):
                st.append(i+1)
            for z in range(1, (st[-1])):
                st.append((st[-1]-z))
            st.append(0)
            print(st)
            break
        else:
            st.append(0)
            for i in range(1, (range_fill // 2)):
                st.append(i)
            for z in range(1, st[-1]):
                st.append(st[-1]-z)
            st.append(0)
            print(st)
            break


        #print(ranges[i])
        #print(ranges[i+1])

    for i in range(len(zero_indexes)):
        st.append(0)

    print(ranges)
    print(zero_indexes)


alg(x, y)
