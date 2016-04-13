import random
import simpy
from mpi4py import MPI
import sys

# ================Service Hub================
class ServiceHub(object):
    """A servicehub has a limited number of trucks (``NUM_TRUCKS``) to
    serve aircrafts in parallel.

    Aircrafts have to request one of the trucks. When they got one, they
    can start the service processes and wait for it to finish (which
    takes ``XXXXTIME`` minutes).

    """
    def __init__(self, env, num_trucks1, num_trucks2, num_trucks3, cleantime, watertime, powertime):
        self.env = env
        self.truck1 = simpy.Resource(env, num_trucks1)
        self.truck2 = simpy.Resource(env, num_trucks2)
        self.truck3 = simpy.Resource(env, num_trucks3)
        self.cleantime = cleantime
        self.watertime = watertime
        self.powertime = powertime

    def clean(self, aircraft):
        """The cleaning processes. It takes a ``aircraft`` processes and tries
        to clean it."""
        print("test")
        if truck1 != 0:
            self.truck1 = self.truck1 - 1
            yield self.env.timeout(CLEANTIME)
            print("servicehub has removed %d%% of %s's dirt." %
                  (random.randint(50, 99), "a1"))
        else:
            print("Pending for service!")

    def water(self, aircraft):
        """The water supply processes. It takes a ``aircraft`` processes and tries
        to supply water it."""
        if truck2 != 0:
            self.truck1 = self.truck1 - 1
            yield self.env.timeout(WATERTIME)
            print("servicehub has supplied %d%% of %s's water." %
                  (random.randint(50, 99), aircraft))
        else:
            print("Pending for service!")

    def power(self, aircraft):
        """The power supply processes. It takes a ``aircraft`` processes and tries
        to power it."""
        if truck3 != 0:
            self.truck1 = self.truck1 - 1
            yield self.env.timeout(POWERTIME)
            print("servicehub has charged %d%% of %s's power." %
                  (random.randint(50, 99), aircraft))
        else:
            print("Pending for service!")


env = simpy.Environment()

sh = ServiceHub(env, 2, 2, 2, 10, 10, 10)


env.run(until=5)

comm = MPI.COMM_WORLD

size = comm.Get_size()

rank = comm.Get_rank()

name = MPI.Get_processor_name()

if rank == 0:
    data = {'a':7, 'b':3.14}
    comm.send(data, dest=0, tag=11)
    print ("Message sent, data is:", data)
elif rank == 0:
    data = comm.recv(source=0, tag=11)
    print ("Message received, data is:", data)