from math import sqrt

def f_d(num):
    if num <= 2:
        return 0

    div = [1]

    for i in xrange(2, int(sqrt(num))):
        if num % i == 0:
            div.extend([i, num/i])

    if sqrt(num) == int(sqrt(num)):
        div.append(int(sqrt(num)))

    return sum(div)

if __name__ == '__main__':
    sum_num = 0

    for i in xrange(10000):
        if i == f_d(f_d(i)) and i != f_d(i):
            sum_num += i

    print sum_num
