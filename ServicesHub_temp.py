import random

import simpy

RANDOM_SEED = 42
NUM_TRUCKS = 2  # Number of trucks in the servicehub
CLEANTIME = 10      # Minutes it takes to clean an aircraft
WATERTIME = 10      # Minutes it takes to supply water to an aircraft
POWERTIME = 10      # Minutes it takes to power up an aircraft
T_INTER = 30       # Create a aircraft every ~30 minutes
SIM_TIME = 120     # Simulation time in minutes


class ServiceHub(object):
    """A servicehub has a limited number of trucks (``NUM_TRUCKS``) to
    serve aircrafts in parallel.

    Aircrafts have to request one of the trucks. When they got one, they
    can start the service processes and wait for it to finish (which
    takes ``XXXXTIME`` minutes).

    """
    def __init__(self, env, num_trucks, cleantime, watertime, powertime):
        self.env = env
        self.truck = simpy.Resource(env, num_trucks)
        self.cleantime = cleantime
        self.watertime = watertime
        self.powertime = powertime

    def clean(self, aircraft):
        """The cleaning processes. It takes a ``aircraft`` processes and tries
        to clean it."""
        yield self.env.timeout(CLEANTIME)
        print("servicehub has removed %d%% of %s's dirt." %
              (random.randint(50, 99), aircraft))

    def water(self, aircraft):
        """The water supply processes. It takes a ``aircraft`` processes and tries
        to supply water it."""
        yield self.env.timeout(WATERTIME)
        print("servicehub has supplied %d%% of %s's water." %
              (random.randint(50, 99), aircraft))

    def power(self, aircraft):
        """The power supply processes. It takes a ``aircraft`` processes and tries
        to power it."""
        yield self.env.timeout(POWERTIME)
        print("servicehub has charged %d%% of %s's power." %
              (random.randint(50, 99), aircraft))


def aircraft(env, name, sh):
    """The aircraft process (each aircraft has a ``name``) arrives at the servicehub
    (``sh``) and requests a service truck.

    It then starts the service process, waits for it to finish and
    leaves to never come back ...

    """
    print('%s arrives at the servicehub at %.2f.' % (name, env.now))
    with sh.truck.request() as request:
        yield request

        print('%s enters the servicehub at %.2f.' % (name, env.now))
        yield env.process(sh.clean(name))

        print('%s leaves the servicehub at %.2f.' % (name, env.now))


def setup(env, num_trucks, cleantime, watertime, powertime):
    """Create a servicehub, a number of initial aircrafts and keep creating aircrafts
    approx. every ``t_inter`` minutes."""
    # Create the servicehub
    servicehub = ServiceHub(env, num_trucks, cleantime, watertime, powertime)

    # Create 4 initial aircrafts
    for i in range(4):
        env.process(aircraft(env, 'aircraft %d' % i, servicehub))

    # Create more aircrafts while the simulation is running
    while True:
        yield env.timeout(random.randint(t_inter-2, t_inter+2))
        i += 1
        env.process(aircraft(env, 'aircraft %d' % i, servicehub))


# Setup and start the simulation
print('Service Hub')
random.seed(RANDOM_SEED)  # This helps reproducing the results

# Create an environment and start the setup process
env = simpy.Environment()
env.process(setup(env, NUM_TRUCKS, CLEANTIME, WATERTIME, POWERTIME))

# Execute!
env.run(until=SIM_TIME)