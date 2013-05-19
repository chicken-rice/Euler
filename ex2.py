if __name__ == '__main__':
    max_num = 4000000
    sum_even = 0	//sum of evwn number
    mod_3 = 2
    num = [1, 2]	//starting number
    p = 1

    while num[p] < max_num:
        mod_3 = (mod_3 + 1) % 3

        if mod_3 == 0:
            sum_even += num[p]

        p = 1 - p
        num[p] = num[0] + num[1]

    print "sum = ", sum_even
