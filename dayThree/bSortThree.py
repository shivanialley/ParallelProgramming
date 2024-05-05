#!/usr/bin/python3
def bubbleSort(lst):
    size = len(lst)
    for i in range(size):
        swap = False
        for j in range(size-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] =lst[j+1],lst[j]
                swap = True

        if swap is False:#one time it will compare
            break

if '__main__' == __name__:
    from sys import argv,exit
    from random import randint
    from time import perf_counter
    from threading import Thread
    if len(argv) <= 1:
        print('Pass some argument')
        exit(1)
    
    size = int(argv[1])
    lst = [randint(1,size *10) for _ in range(size)]
    start = perf_counter()
    print("Before List: " ,lst)
    iObj = Thread(target=bubbleSort, args = [lst])#first time sorting
    iObj.start()
    iObj.join()
    print("After List: ",lst)
    end=perf_counter()
    print(f"Time Taken: {round(end-start,3)}")
