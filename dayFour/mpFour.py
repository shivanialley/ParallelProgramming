#!/usr/bin/python3

import multiprocessing as mp 
from time import sleep, perf_counter
from os import getpid

def doSomeJob():
    print(f'Job Started...{getpid()}')
    sleep(1)
    print(f'Job Completed...')
    print('*' * 40)

if __name__ == '__main__':
    print(f'Main process {getpid()}')
    start = perf_counter()
    listObjs = []
    for _ in range(3):
        pObj = mp.Process(target=doSomeJob)
        listObjs.append(pObj)
    for each in listObjs:
        each.start()
    for one in listObjs:
        one.join()

    end = perf_counter()

    print(f'Time taken: {round(end-start,3)} secs')
