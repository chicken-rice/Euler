from math import sqrt

def judge_prime(int_num):
    for i in xrange(2, int(sqrt(int_num))+1):
        if int_num % i == 0:
            return False

    return True

if __name__ == '__main__':
    count = 1
    last_prime = 2
    int_num = 3

    while count < 10001:
        if judge_prime(int_num):
            last_prime = int_num 
            count += 1
        int_num += 2

    print last_prime
