from math import sqrt

def print_product(num):
    root = int(sqrt(num))

    for i in xrange(root, 1000):
        if (num % i) == 0:
            print i, num/i, num
            return True

    return False

def is_palindrome(num):
    num_str = str(num)

    if num_str == ''.join(reversed(num_str)):
        return True
    return False

if __name__ == '__main__':
    for i in xrange(999*999, 100*100, -1):
        if is_palindrome(i):
            if print_product(i):
                break;
            
