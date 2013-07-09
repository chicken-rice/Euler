def read_file():
    in_int = []

    for line in open('ex11.txt'):
        line_split = line[:-1].split()
        in_int.append( map(int, line_split) )

    return in_int

def product_4(data, x, y, dx, dy):
    len_y = len(data[0])
    len_x = len(data)

    if x+3*dx >= len_x or y+3*dy >= len_y:
        return 0
    else:
        pro = 1
        for i in xrange(4):
            pro *= data[y+i*dy][x+i*dx]
        return pro
        

if __name__ == '__main__':
    data = read_file()

    r = lambda data, x, y: product_4(data, x, y, 1, 0)
    u = lambda data, x, y: product_4(data, x, y, 0, 1)
    ur = lambda data, x, y: product_4(data, x, y, 1, 1)
    ul = lambda data, x, y: product_4(data, x, y, -1, 1)

    func = [r, u, ur, ul]
    val = []

    for i in xrange(len(data)):
        for j in xrange(len(data[0])):
            for f in func:
                val.append(f(data, j, i))

    print max(val)
