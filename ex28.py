def diagonal(num):
    vert_sum = lambda x: 2 * (2*(2*x-1)**2 - 6*(x-1))
    sum_num = 1
    sum_num +=  sum(map(vert_sum, xrange(2, (num+3)/2)))

    return sum_num

if __name__ == '__main__':
    print diagonal(1001)
