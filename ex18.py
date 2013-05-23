def read_file():
    in_int = []

    for line in open('ex18.txt'):
        line_split = line[:-1].split()
        in_int.append([0] + map(int, line_split) + [0])

    return in_int

def dynamic(child, parent_1, parent_2):
    if parent_1 > parent_2:
        return child + parent_1
    else:
        return child + parent_2

if __name__ == '__main__':
    data = read_file()

    for i in xrange(1, len(data)):
         data[i] = [0] + map(dynamic, data[i][1:-1], data[i-1][:-1], data[i-1][1:]) + [0]

    print max(data[-1])
