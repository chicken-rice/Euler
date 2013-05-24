def read_file():
    text = open('ex22.txt').read()
    data = text.replace('"', '').split(',')
    data.sort()
    return [''] + data

def calc_worth(name, index):
    al_num = lambda char: ord(char) - ord('A') + 1

    return index * sum(map(al_num, list(name)))

if __name__ == '__main__':
    data = read_file()

    print sum(map(calc_worth, data, xrange(len(data))))
