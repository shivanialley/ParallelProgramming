
if '__main__' == __name__:
    from sys import argv

    if len(argv) > 1:
        print('Good args are passed...',*argv)
        sum = 0
        for temp in argv[1:]:
            sum += int(temp)
        print('Sum of number  ',sum)
    else:
        print('Not Good args are not passed.....')
