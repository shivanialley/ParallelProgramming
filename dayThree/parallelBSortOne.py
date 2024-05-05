#!/usr/bin/python3

from time import perf_counter
from random import randint
from threading import Thread

def evenPhase(lst,n):
    for i in range(0, n-1, 2):
        if lst[i] > lst[i+1]:
            lst[i],lst[i+1] = lst[i+1],lst[i]
def oddPhase(lst,n):
    for i in range(1, n-1, 2):
        if lst[i] > lst[i+1]:
            lst[i],lst[i+1] = lst[i+1],lst[i]

def bSort(lst):
    n = len(lst)
    threadObjs = []
    for i in range(1,n+1):
        if i%2 == 0:
            t1obj = Thread(target=evenPhase, args = [lst, n])
            t1obj.start()
            threadObjs.append(t1obj)
        else:
            t2Obj = Thread(target = oddPhase,args = [lst,n])
            t2Obj.start()
            threadObjs.append(t2Obj)
    for thread in threadObjs:
        thread.join()

if '__main__' == __name__:
    from sys import argv,exit
    from random import randint

    if len(argv) <= 1:
        print("Pass argument")
        exit(1)

    size = int(argv[1])
    lst = [randint(1,size *10) for _ in range(size)]
    start = perf_counter()
    print("Before List: " ,lst)
    bSort(lst)
    print("After List: ",lst)
    end = perf_counter()
    print(f"Time taken: {round(end-start,3)}")
