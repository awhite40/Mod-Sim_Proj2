
# Recieve messages - process them in timestamp order

# List of variables
    # Airport gates
        # Requests services
    # Airplane queue
# When service indicates that it is available send it message of where to go next
import numpy
from mpi4py import MPI
from MPI import ANY_SOURCE
def Generate_airplane(ID):
    Plane_ID = ID
    if Gate_1_free == TRUE:
        Plane_Gate = 'Gate 1'
        Gate_1_free == FALSE
        comm.Send(Plane_Gate, dest = 1) #Schedule first service
    else if Gate_2_free ==TRUE:
        Plane_Gate = 'Gate 2'
        Gate_2_free = FALSE
        comm.Send(Plane_Gate, dest = 1) #Schedule first service
    else if Gate_3_free ==TRUE:
        Plane_Gate = 'Gate 3'
        Gate_3_free = FALSE
        comm.Send(Plane_Gate, dest = 1) #Schedule first service
    else if Gate_4_free ==TRUE:
        Plane_Gate = 'Gate 4'
        Gate_4_free = FALSE
        comm.Send(Plane_Gate, dest = 1) #Schedule first service
    else:
        #Add plane to queue
    return Plane_Gate

comm = MPI.COMM_WORLD
rank = comm.Get_rank()


if rank ==0:

    Gate_1_free = TRUE
    Gate_2_free = TRUE
    Gate_3_free = TRUE
    Gate_4_free = TRUE

    Gate = Generate_airplane(ID)
    comm.Recv(info, source = ANY_SOURCE)
    

