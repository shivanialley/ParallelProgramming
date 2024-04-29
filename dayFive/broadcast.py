'''
        Simple Hello World
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD #Default communicator
rank = comm.Get_rank()

if rank == 0:
    data = 'Some data to be send....'
else:
    data = None#none is datatype

data = comm.bcast(data, root = 0)
print(f'Rank: {rank} data: {data}')