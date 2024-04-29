'''
        Simple Hello World
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD #Default communicator
rank = comm.Get_rank()

print(f"Hello World from {rank} ")