if __name__ == '__main__':
    a = 100
    b = 100
    calc = []

    for i in xrange(2, a+1):
        for j in xrange(2, b+1):
            calc.append(i**j)

    calc = set(calc)

    print len(calc)
