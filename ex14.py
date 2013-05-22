if __name__ == '__main__':
    max_num = 0
    col_num = 8
    last_num = 0
    flag_end = False


    count = 0

    while(True):
        print col_num
        count += 1
        if count == 200:
            break
        if (col_num-1)%3 == 0\
        and (col_num-1)/3%3 != 0\
        and (col_num-1)/3%2 != 0:
          #  last_num = col_num
            col_num = (col_num-1) / 3
            if col_num >= 100**6:
                break
        else:
         #   last_num = col_num
            col_num *= 2

        if col_num < 10**6 and max_num < col_num:
                max_num = col_num

    print max_num 
