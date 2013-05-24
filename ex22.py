def read_file():
    text = open('ex22.txt').read().split(',')
    data = text.replace('"', '').sort()
    
    return [''] + data


if __name__ == '__main__':
    al_num = lambda char: ord(char) - ord('A') + 1
    calc_worth = lambda name, index:\
                     index * sum(map(al_num, list(name)))

    data = read_file()
    print sum(map(calc_worth, data, xrange(len(data))))
