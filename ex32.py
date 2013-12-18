def isPandigital(num_string):
    if not isSingle(num_string) or len(num_string) != 9:
        return False

    return True

def isSingle(num_string):
    list_num = list(num_string)
    set_num = list(set(num_string))
    list_num.sort()
    set_num.sort()
    return list_num == set_num


if __name__ == '__main__':
    ans_list = []

    for i in xrange(10**2):
        if str(0) in str(i) or not isSingle(str(i)):
            continue

        for j in xrange(10**4):
            if i*j > 10**10:
                break

            if str(0) in str(j) or not isSingle(str(i)+str(j)):
                continue

            if str(0) not in str(i*j) and isPandigital(str(i)+str(j)+(str(i*j))):
                if i*j not in ans_list:
                    ans_list.append(i*j)
		print i,'*',j,'=',i*j


    print ans_list
    print sum(ans_list)
