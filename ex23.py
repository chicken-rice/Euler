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

    #for abun in abun_list:
     #   if abun > num:
     #       break
     #   if (num-abun) in abun_list:
     #       return True

   # return False


def get_sum_of_abun(num, abun_list):
    if is_sum_of_abun(num, abun_list):
        return num
    else:
        return -1


if __name__ == '__main__':
    sum_num = 0
    max_num = 28124
    #max_num = 5000

    abun_list = list(set(map(get_abun, xrange(12, max_num))))
    abun_list.remove(-1)
    get_SOA = lambda num: get_sum_of_abun(num, abun_list)

#    odd = lambda num: num % 2 == 1
#    even = lambda num: num % 2 == 0

#    odd_list = map(odd, abun_list)
#    even_list = map(even, abun_list)
    #3print 'test'
#    print 'kisu'
#    print sum(odd_list)
#    print sum(even_list)
#    print odd_list.index(True)
#    print abun_list[odd_list.index(True)]

    SOA_list = list(set(map(get_SOA, xrange(12, max_num))))
    SOA_list.remove(-1)

    #abun_list.sort()
    #SOA_list.sort()
#    print abun_list[:100]
#    print 'len', len(abun_list)
    #print SOA_list
    print sum(SOA_list)
#    for i in range(12, 28123 + 1):
 #       if is_abundant(i):
  #          abun_list.append(i)
   #     if is_sum_abun(i, abun_list):
    #        sum_num += i

 #   print sum_num
#    
