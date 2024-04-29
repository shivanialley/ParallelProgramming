'''
        Simple Hello World
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD #Default communicator
rank = comm.Get_rank()

if rank == 0:
    data = 'Hello'
    print(f"First processor sending....{data}")
    comm.send(data,dest =1)
elif rank == 1:
    data = comm.recv(source = 0)
    print(f'Recieved data from first processor:{data}')