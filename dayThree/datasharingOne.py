#!/usr/bin/python3

from os import getpid
from threading import Thread
from time import sleep

data = 10

def myFun():
    global data
    print(f'Remember....{getpid()}---> data:{data}')
    for _ in range(10):
        data+=1
    print('*'*40)

if __name__ == "__main__":
    print(f'In main...{getpid()}')
    for _ in range(10):
        data+=1
    t1 =Thread(target=myFun())
    t1.start()
    
    print('-'*40)
    for _ in range(10):
            data+=1
    t2 =Thread(target=myFun())
    t2.start()

    t1.join()
    t2.join()
    print('$'*40)
    print(f"Finally before exiting data: {data}")
