def get_rec_num(num, div_list):
    count = 0
    current = num

    print 'get'
    while div_list[current] != 0:
        temp = current
        current = div_list[current]
        print current, div_list[current]
        div_list[temp] = 0
        count += 1

    return count

def recur_cycle(nume, deno, div_list):
    print nume, deno, div_list
    dec_nume = nume
    div_num = 0
    while div_num == 0:
        dec_nume *= 10
        div_num = dec_nume / deno
        mod_num = dec_nume % deno

    if mod_num == 0:
        return 0

    div_list[dec_nume/10] = mod_num
 
    if div_list[mod_num] == 0:
        #print mod_num, deno, div_list
        return recur_cycle(mod_num, deno, div_list)
    else:
        return get_rec_num(mod_num, div_list)

if __name__ == '__main__':
    num = 17 
    print recur_cycle(1, num, [0 for i in xrange(10*num)])
