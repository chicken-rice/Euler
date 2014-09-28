def get_rec_num(num):
    table = [-1 for i in range(num*10+1)]
    temp_num = 1
    count = 0

    while True:
        if temp_num == 0:
            return 0

        div_num = 0
        while div_num == 0:
            temp_num *= 10
            div_num = temp_num / num
            count += 1

        if table[temp_num] != -1:
            return count - table[temp_num]
        else:
            table[temp_num] = count
            temp_num = temp_num % num

if __name__ == '__main__':
    max_rec = 0
    max_num = 0
    for i in xrange(1, 1000):
        temp_rec = get_rec_num(i)
        if max_rec < temp_rec:
            max_rec = temp_rec
            max_num = i

    print "ans", max_num
