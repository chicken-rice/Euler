from math import sqrt

def judge_prime(int_num):
    for i in xrange(2, int(sqrt(int_num))+1):
        if int_num % i == 0:
            return False

    return True

if __name__ == '__main__':
    sum_num = 2

    for i in xrange(3, 2000000, 2):
        if judge_prime(i):
            sum_num += i

    print sum_num
