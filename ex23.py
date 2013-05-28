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
    
def is_sum_of_abun(num, abun_list):
    is_true = lambda abun: (num-abun) in abun_list
    return any(map(is_true, abun_list))

def get_sum_of_abun(num, abun_list):
    if is_sum_of_abun(num, abun_list):
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
    sum_num = 0
    max_num = 28124 + 40
    max_num = 5000
    max_num = 28124

    abun_list = list(set(map(get_abun, xrange(12, max_num))))
    abun_list.remove(-1)
    abun_list.sort()
    get_SOA = lambda num: get_sum_of_abun(num, abun_list)

    odd = lambda num: num % 2 == 1
    even = lambda num: num % 2 == 0

    odd_flag = map(odd, abun_list)
    even_flag = map(even, abun_list)
    
    print abun_list[odd_flag.index(True)]
    print abun_list[even_flag.index(True)]

    odd_list = get_list(abun_list, odd_flag)
    even_list = get_list(abun_list, even_flag)
    print odd_list

    num_list = range(max_num)
    num_list = reduce_list(odd_list, even_list, num_list)
    print 'odd even', len(num_list)
    num_list = reduce_list(even_list, even_list, num_list)
    print 'even, even', len(num_list)
    num_list = reduce_list(odd_list, odd_list, num_list)
    print sum(num_list), 'odd odd',len(num_list)

    temp = []
    last = 0
    for i in odd_list:
        temp.append(i-last)
        last = i

    #print temp
#    SOA_list = list(set(map(get_SOA, xrange(12, max_num))))
#    SOA_list.remove(-1)

    #abun_list.sort()
    #SOA_list.sort()
#    print abun_list[:100]
#    print 'len', len(abun_list)
    #print SOA_list
#    print sum(SOA_list)
#    for i in range(12, 28123 + 1):
 #       if is_abundant(i):
  #          abun_list.append(i)
   #     if is_sum_abun(i, abun_list):
    #        sum_num += i

 #   print sum_num
#    
