x = 20
y = '10 13 31 35 39 0 0 59 0 66 68 73 74 0 0 0 87 89 96 99'.split(' ') # answer: 0 1 2 1 0
#x = int(input())
#y = input().split(' ')

def alg(n, points):
    counter = 0
    ranges = []
    zero_indexes = []
    popped = []
    for i in points:
        if i == '0':
            zero_indexes.append(points.index(i))
            points[points.index(i)] = '00'
            #points.pop(points.index(i))

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

    #st.append(0)

    if len(ranges) == 1:
        for i in range(x):
            st.append(i)
        return print(st)
    for i in range(len(ranges) - 1):
        #print(i)
        if i == 0 and ranges[i] > 0:
            for z in range(ranges[0]):
                st.append(ranges[0] - z)
            st.append(0)

        range_fill = abs(ranges[i+1])
        if range_fill == 0:
            range_fill = ranges[i]
        if ranges[i+1] < ranges[i] and i > 0:
            range_fill = ranges[i+1]
        print(f'range_fill = {range_fill}')
        if range_fill % 2:
            if range_fill == 1:
                st.append('11')
            #print('yes')
            if i < 1:
                st.append(0)
            for i in range((range_fill // 2) + 1):
                st.append(i+1)
            previous_length = st[-1]
            for z in range(1, previous_length):
                st.append((previous_length-z))
            st.append(0)
            #print(st)
        else:
            #if i < 1:
            #    for i in range(x):
            #        st.append(i)
            #    print(st)
            #    break
            #else:

            if i < 1:
                st.append(0)
            #print('tru')
            for i in range(1, (range_fill // 2)+1):
                st.append(i)
            previous_length = st[-1]
            for z in range(1, (range_fill // 2) + 1):
                st.append((previous_length + 1) - z)
            st.append(0)
    #if ranges[0] > 0:
    #    print('sf')
    #    st.pop(st[0])
    print(' '.join(str(x) for x in st))

        #print(ranges[i])
        #print(ranges[i+1])

    #for i in range(len(zero_indexes)):
    #    st.append(0)

    print(f'ranges = {ranges}')
    print(f'zero indexes = {zero_indexes}')


alg(x, y)
