
def fibonacii(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0,1]
    else:
        fib_series = [0,1]
        for i in range(2,num):
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

if '__main__' == __name__:
    from sys import argv

    if len(argv) > 1:
        print('Good args are passed...',*argv)
        temp = int(argv[1])
        fib_series=fibonacii(temp)
        print("Fibonacci series:")
        print(fib_series)
    else:
        print('Not Good args are not passed.....')
