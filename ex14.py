def calc_chain(num, data = [-1 for i in xrange(10**8)]):

    if data[num] != -1:
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
        #print chain_num[i]
        #if i > 30:
        #    break

    print max(xrange(len(chain_num)), key=lambda i: chain_num[i])
