
def bubble(num)
    mylist = []
   for i in range(0,num):
       for j in range (0,num):


if '__main__' == __name__:
    from sys import argv

    if len(argv) > 1:
        print('Good args are passed...',*argv)
        temp = int(argv[1])
        bubble_sort=bubble(temp)
        print("Fibonacci series:")
        print(bubble_sort)
    else:
        print('Not Good args are not passed.....')
