from math import sqrt

def judge_prime(int_num):
    for i in xrange(2, int(sqrt(int_num))+1):
        if int_num % i == 0:
            return False

    return True

if __name__ == '__main__':
    num = 600851475143
    sqrt_num = int(sqrt(num))
    if sqrt_num % 2 == 0:
        sqrt_num -= 1 

    for i in xrange(sqrt_num, 1, -2):
        if num % i == 0 and judge_prime(i):
            print i
            break
