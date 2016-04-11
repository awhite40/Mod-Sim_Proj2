
# Recieve messages - process them in timestamp order

# List of variables
    # Airport gates
        # Requests services
    # Airplane queue
# When service indicates that it is available send it message of where to go next
import numpy
from mpi4py import MPI
from MPI import ANY_SOURCE
import simpy

def Generate_airplane(ID):
    Plane_ID = ID
    if Gate_1_free == True:
        Plane_Gate = 'Gate 1'
        Gate_1_free = False
        comm.Send(Plane_Gate, dest = 1)  # Schedule first service
    elif Gate_2_free == True:
        Plane_Gate = 'Gate 2'
        Gate_2_free = False
        comm.Send(Plane_Gate, dest=1)  # Schedule first service
    elif Gate_3_free == True:
        Plane_Gate = 'Gate 3'
        Gate_3_free = False
        comm.Send(Plane_Gate, dest=1)  # Schedule first service
    elif Gate_4_free == True:
        Plane_Gate = 'Gate 4'
        Gate_4_free = False
        comm.Send(Plane_Gate, dest=1)  # Schedule first service
    else:
        plane_queue = plane_queue + 1
        #Add plane to queue
    Departure_time = env.Now() + 30*60  # Now + 30 mins?
    return Plane_Gate, Departure_time, Plane_ID

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
plane_queue = 0

if rank == 0:
    env = simpy.Environment()
    Gate_1_free = True
    Gate_2_free = True
    Gate_3_free = True
    Gate_4_free = True
    ID = 1
    Gate, Departure_time, Plane_ID = Generate_airplane(ID)
    comm.Recv(info, source=ANY_SOURCE)


