from math import factorial

def dict_num(num, parts):

    if len(parts) == 1:
        return parts

    fact = factorial(len(parts)-1)
    div_num = num / fact
    mod_num = num % fact

    return [parts.pop(div_num)] + dict_num(mod_num, parts)

if __name__ == '__main__':
    num_list = dict_num(10**6-1, range(10))
    print "".join(map(str, num_list))
