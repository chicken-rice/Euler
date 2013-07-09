from math import sqrt

def is_abundant(num):
    div = [1]

    for i in xrange(2, int(sqrt(num))+1):
        if num % i == 0:
            div.extend([i, num/i])

    if int(sqrt(num)) == sqrt(num):
        div.remove(int(sqrt(num)))

    return sum(div) > num


def get_abun(num):
    if is_abundant(num):
        return num
    else:
        return -1

def get_list(abun, flag):
    mul = lambda a, f: a*f
    fil_list = set(map(mul, abun, flag))
    fil_list.discard(0)
    fil_list2 = list(fil_list)
    fil_list2.sort()
    return fil_list2

def reduce_list(list1, list2, num_list):
    for i in list1:
        func1 = lambda x: x - i
        func2 = lambda x: x + i

        func1_list = map(func1, num_list)
        inter_set = set(func1_list).intersection(set(list2))
        func2_list = map(func2, inter_set)
        num_list = list(set(num_list).difference(set(func2_list)))

    return num_list
        

if __name__ == '__main__':
    max_num = 28124

    abun_list = list(set(map(get_abun, xrange(12, max_num))))
    abun_list.remove(-1)
    abun_list.sort()

    odd = lambda num: num % 2 == 1
    even = lambda num: num % 2 == 0

    odd_flag = map(odd, abun_list)
    even_flag = map(even, abun_list)
    odd_list = get_list(abun_list, odd_flag)
    even_list = get_list(abun_list, even_flag)

    num_list = range(max_num)
    num_list = reduce_list(odd_list, even_list, num_list)
    print 'odd even', len(num_list)
    num_list = reduce_list(even_list, even_list, num_list)
    print 'even, even', len(num_list)
    num_list = reduce_list(odd_list, odd_list, num_list)
    print 'odd odd',len(num_list)
    print 'sum', sum(num_list)
