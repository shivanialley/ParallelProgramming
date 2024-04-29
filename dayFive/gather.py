'''
        Simple gather sub array from multiple processes and store in full array
'''

from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD #Default communicator
rank = comm.Get_rank()
size = comm.Get_size() #gives total number of process (-n 4)

dataPerRank = 10
sendData = np.linspace(rank * dataPerRank + 1,(rank + 1) * dataPerRank,dataPerRank)

    #if rank = 0 ---> linespace(1,10,10)
    #if rank = 1 ---> linespace(11,20,10)

recvData = None
if rank ==0:
    recvData = np.empty(dataPerRank * size, dtype = 'd')
else: 
    print(f"rank: {rank} sending: {sendData}")
comm.Gather(sendData, recvData,root = 0)

if rank == 0:
    print(f'rank -->{rank} --->recvData: {recvData}')