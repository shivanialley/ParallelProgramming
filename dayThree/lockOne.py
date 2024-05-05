#!/usr/bin/python3

from time import sleep
from random import randint
from threading import Thread, Lock

def doSomeJob(lock, ident, value):
    #acquire the lock
    with lock:
        print(f"Thread ID: {ident} got the lock going to sleep for  {value} secs")
        sleep(value)


if '__main__' == __name__:
    lock = Lock()
    for i in range(5):
        Thread(target=doSomeJob,args=(lock,i+1,randint(1,3))).start()
