if __name__ == '__main__':
    ans = 1

    for i in xrange(1, 10**12+1):
        ans *= i
    	while ans % 10 == 0:
	    ans /= 10
        ans %= 10**7
    
    #ans = ans ** (10**8)
    print ans
    exit()

    for i in xrange(8):
        ans = ans ** 10
        while ans % 10 == 0:
            ans /= 10
        ans %= 10**8

    ans %= 10**6

    print ans
