#!/usr/bin/python3

from time import sleep
from threading import Thread

class MyThread(Thread):
    def __init__(self,arg=10):
        super().__init__()
        self.value = arg

    def run(self):
        print(f"Job Started..")
        sleep(1)
        print(f"Job Completed..")
        self.value = self.value + 100

if __name__ == "__main__":
    tObj = MyThread(20)
    tObj.start()
    print("Waiting for child thread to complete")
    tObj.join()
    result = tObj.value;
    print(f"Value from thread: {result}")
