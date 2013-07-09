if __name__ == '__main__':
    get_digit = lambda num: len(str(num))

    fib_last = 0
    fib_curr = 1
    fib_count = 1

    while get_digit(fib_curr) < 10**3:
        fib_temp = fib_curr
        fib_curr += fib_last
        fib_last = fib_temp
        fib_count += 1

    print fib_count
