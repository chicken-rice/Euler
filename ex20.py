if __name__ == '__main__':
    fact = 1
    for i in xrange(1, 101):
        fact *= i

    print sum(map(int, list(str(fact))))
