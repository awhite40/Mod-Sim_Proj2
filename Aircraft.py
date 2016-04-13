import random
import simpy
from mpi4py import MPI

import ServicesHub
import Aircraft
# ================Aircrafts================

class Aircraft(Object):
    """The aircraft process (each aircraft has a ``name``) arrives at the servicehub
    (``sh``) and requests a service truck.

    It then starts the service process, waits for it to finish and
    leaves to never come back ...

    """
    def __init__(self, env, name, size):
        self.env = env
        self.name = name
        self.size = size

    print('%s arrives at the servicehub at %.2f.' % (name, env.now))


    with sh.truck.request() as request:
        yield request

        print('%s enters the servicehub at %.2f.' % (name, env.now))
        yield env.process(sh.clean(name))

        print('%s leaves the servicehub at %.2f.' % (name, env.now))