def read_file():
    in_string = open('ex8.txt').read()
    in_string = in_string.replace('\n', '')
    in_int = map(int, list(in_string))
    return in_int

if __name__ == '__main__':
    max_mul = 0
    temp_i = 0
    data = read_file()

    for i in xrange(len(data)-4):
        calc_mul = data[i] * data[i+1] * data[i+2] * data[i+3] * data[i+4]
        if calc_mul > max_mul:
            max_mul = calc_mul
            temp_i = i
    print max_mul
    print temp_i
