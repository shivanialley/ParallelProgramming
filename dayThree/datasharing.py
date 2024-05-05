#!/usr/bin/python3

from os import getpid
from threading import Thread
from time import sleep

def myFun():
    print(f'Remember....{getpid()}')
    sleep(1)
    print('*'*40)

if __name__ == "__main__":
    print(f'In main...{getpid()}')
    t1 =Thread(target=myFun())
    t1.start()
    t1.join()
    print('-'*40)
    t2 =Thread(target=myFun())
    t2.start()
    t2.join()
    print('$'*40)
