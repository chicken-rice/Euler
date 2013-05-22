def calc_chain(num, data = {}):

    if num in data:
        return data[num]

    if num == 1:
        data[1] = 1
    elif num % 2 == 0:
        data[num] = calc_chain(num/2) + 1
    else:
        data[num] = calc_chain(3*num+1) + 1
       
    return data[num] 

if __name__ == '__main__':
    chain_num = [0 for i in xrange(10**6)]

    for i in xrange(1, 10**6):
        chain_num[i] = calc_chain(i)

    max_index = max(xrange(len(chain_num)), key=lambda i: chain_num[i])
    print max_index, chain_num[max_index]
