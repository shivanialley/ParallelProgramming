"""
multi-processing with arguments
"""
from multiprocessing import Pool
from time import sleep, perf_counter
from os import  getpid

def doSomeJob(args):
    print(f'Job Started....{getpid()},{args}')
    sleep(args)
    print(f'Job Completed...')
    print('*' * 40)
    print(f'{args} Job Completed...with {getpid()}')

if __name__== '__main__':
    start =perf_counter()
    with Pool(3) as pobj:
        print(pobj.map(doSomeJob, [1,1,2]))
    end = perf_counter()

    print(f'Time taken: {round(end-start,3)} secs')
