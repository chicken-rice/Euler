from calendar import weekday

if __name__ == '__main__':
    count = 0

    for y in xrange(1901, 2001):
        for m in xrange(1, 13):
            if weekday(y, m, 1) == 6:
                count += 1

    print count
