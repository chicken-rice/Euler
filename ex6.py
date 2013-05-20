if __name__ == '__main__':
    sum_sqr = 0
    sqr_sum = 0

    for i in xrange(100+1):
        sum_sqr += i**2
        sqr_sum += i

    print sqr_sum**2 - sum_sqr
