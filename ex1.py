if __name__ == '__main__':
    sum = 0
    max = 1000

    for i in (3, 5):
        for j in xrange(i, max, i):
            sum += j

    for i in xrange(15, max, 15):
        sum -= i

    print sum
