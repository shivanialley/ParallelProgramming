'''
        Simple Scatter an array to multiple process and subarrays
'''

from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD #Default communicator
rank = comm.Get_rank()
size = comm.Get_size() #gives total number of process (-n 4)
Sendingdata = None
dataPerRank = 10
if rank == 0:
    Sendingdata = np.linspace(1, size * dataPerRank, size *dataPerRank)
    #when -n 4 , here size =4 ---> Sendingdata - {1,0:40,0}
recvdata = np.empty(dataPerRank, dtype='d')
comm.Scatter(Sendingdata,recvdata, root = 0)
print(f'Rank: {rank} data: {recvdata}')