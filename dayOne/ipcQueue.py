"""
working on single process ---- parallelism
"""
from multiprocessing import Process, Queue
from time import sleep, perf_counter
from os import  getpid

def doSomeJob(que):
    print(f'Child Process with....{getpid()}')
    que.put([1001,"Some Name here",34234.4324])
    print(f'Job Completed...')
    print('*' * 40)


if __name__== '__main__':
    start =perf_counter()
    print(f'Parent Process with...{getpid()}') 
    que = Queue()
    pObj = Process(target=doSomeJob,args=(que,))
    pObj.start()#start the process
    print(f'getting...{que.get()}')
    pObj.join()#join the process
    end = perf_counter()

    print(f'Time taken: {round(end-start,3)} secs')
