import time
import numpy as np

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
dispersed_points = 0

def monte_Carlo(points):
    inside_circle = np.count_nonzero(pow(pow((points.T[0]),2) + pow((points.T[1]),2),0.5) <= 1)
    result = (inside_circle/len(points))*4

    return result

def inside_Circle(point):
    p = pow(pow((point[0]),2) + pow((point[1]),2),0.5)

    if p > 1:
        return False 
    else:
        return True



if rank == 0:

    amount = 1000000
    array = np.random.rand(amount, 2)
    divide_size = int(amount / size)

    dispersed_points = [array[0: (i+1) * divide_size]for i in range(0, size)]

points = comm.scatter(dispersed_points, root=0)

start_time = time.perf_counter()
pi_number = monte_Carlo(points)
end_time = time.perf_counter()

processes = comm.gather({"PI": pi_number,"ExecutionTime": (end_time - start_time)}, root=0)

if rank == 0:
    for process in processes:
            print(f'Pi number: {process["PI"]:10f} Execution time: {process["ExecutionTime"]:0.6f}')

#The OS used : Ubuntu
#command for execution: # mpiexec -n 2 python3 main.py
#I used only 2 processes because Ubuntu on virtual machine and I wasn't able to use more than two cores
