if __name__ == '__main__':
    s_1_9 = ['one', 'two', 'trhee', 'four', 'five',
             'six', 'seven', 'eight', 'nine']

    s_10_19 = ['ten', 'eleven', 'twelve', 'thirteen',
               'fourteen', 'fifteen', 'sixteen',
               'seventeen', 'eighteen', 'nineteen']

    s_20_90 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty',
               'seventy', 'eighty', 'ninety']

    
    s_100 = 'hundred'
    s_1000 = 'thousand'
    s_and = 'and'

    c_1_9 = sum(map(len, s_1_9))
    c_10_19 = sum(map(len, s_10_19))
    c_20_90 = sum(map(len, s_20_90))

    c_1_99 = c_1_9 + c_10_19 + 10*c_20_90 + len(s_20_90)*c_1_9
    c_1_1000 = 10*c_1_99 + 900*len(s_100) + 9*99*len(s_and) + 100*c_1_9 + len(s_1000) + len(s_1_9[0])

    print c_1_1000
