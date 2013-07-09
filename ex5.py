def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)

def lcm(num1, num2):
    return num1 * num2 / gcd(num1, num2)

if __name__ == '__main__':
    ans = 2

    for i in xrange(3,20+1):
        ans = lcm(ans, i)

    print ans
