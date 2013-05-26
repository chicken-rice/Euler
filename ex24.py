from math import factorial

def dict_num(num, parts):

    if len(parts) == 1:
        print parts[0]
        return

    fact = factorial(len(parts)-1)
    div_num = num / fact
    mod_num = num % fact

    print parts.pop(div_num),

    dict_num(mod_num, parts)

if __name__ == '__main__':
    dict_num(1000000-1, range(10))
