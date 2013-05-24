from math import sqrt

def is_abundant(num):
    div = [1]

    for i in xrange(2, int(sqrt(num))+1):
        if num % i == 0:
            div.extend([i, num/i])

    if int(sqrt(num)) == sqrt(num):
        div.remove(int(sqrt(num)))

    return sum(div) > num
    
def is_sum_abun(num, abun_list):
    for abun in abun_list:
        if abun > num:
            break
        if (num-abun) in abun_list:
            return True

    return False

if __name__ == '__main__':
    sum_num = 0
    abun_list = []

    for i in range(12, 28123 + 1):
        if is_abundant(i):
            abun_list.append(i)
        if is_sum_abun(i, abun_list):
            sum_num += i

    print sum_num
    
