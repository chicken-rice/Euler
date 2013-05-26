if __name__ == '__main__':
    vert_sum = lambda x: 2 * (2*(2*x-1)**2 - 6*(x-1))
    diagonal = lambda num: 1 + sum(map(vert_sum, xrange(2, (num+3)/2)))

    print diagonal(1001)
