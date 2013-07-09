def read_file():
    in_string = open('ex13.txt').read()
    in_string = in_string[:-1].split('\n')
    in_int = map(int, in_string)
    return in_int

if __name__ == '__main__':
    data = read_file()
    sum_num = sum(data)
    print int(str(sum_num)[:10])
