def funcA(a, b):
    return 1000 * (a + b) - a * b

if __name__ == '__main__':
    for i in xrange(500, 250, -1):
        for j in xrange(1, 251):
            ansA = funcA(i, j)
            if ansA == 500000:
                print i, j
            elif ansA > 500000:
                break
