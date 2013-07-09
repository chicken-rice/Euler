from math import sqrt

def div_num(num):
    count = 0
    for i in xrange(1, int(sqrt(num))+1 ):
        if num % i == 0:
            count += 2
    if int(sqrt(num)) == sqrt(num):
        count -= 1

    return count

if __name__ == '__main__':
    count = 0
    num = 0

    while(True):
        count += 1
        num += count
        if div_num(num) >= 500:
            print num
            break
