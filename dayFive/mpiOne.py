'''
        Simple Hello World
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD #Default communicator
rank = comm.Get_rank()
if rank == 0:
    print(f'Hello world from first processor')
elif rank == 1:
    print(F'Hello World from second processor')
else:
    print("Hello World from others")
