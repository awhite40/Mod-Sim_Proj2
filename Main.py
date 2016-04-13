import random
import simpy
from mpi4py import MPI

# ================Setup================

RANDOM_SEED = 42
NUM_TRUCKS1 = 2     # Number of trucks for cleaning in the servicehub
NUM_TRUCKS2 = 2     # Number of trucks for water supply in the servicehub
NUM_TRUCKS3 = 2     # Number of trucks for power supply in the servicehub
CLEANTIME = 10      # Minutes it takes to clean an aircraft
WATERTIME = 10      # Minutes it takes to supply water to an aircraft
POWERTIME = 10      # Minutes it takes to power up an aircraft
SIM_TIME = 120      # Simulation time in minutes

class Main(env, num_trucks1, num_trucks2, num_trucks3, cleantime, watertime, powertime):
    def __init__(self, env, name, size):
        self.env = env
        self.name = name
        self.size = size
    # Create the servicehub
    servicehub = ServiceHub(env, num_trucks1, num_trucks2, num_trucks3, cleantime, watertime, powertime)
    # Create one aircraft
    aircraft = Aircraft(env, A1)

# Setup and start the simulation
print('Service Hub')
random.seed(RANDOM_SEED)  # This helps reproducing the results

# Create an environment and start the setup process
env = simpy.Environment()
env.process(setup(env, NUM_TRUCKS1, NUM_TRUCKS2, NUM_TRUCKS3, CLEANTIME, WATERTIME, POWERTIME))

# Execute!
env.run(until=SIM_TIME)

if __name__ == '__main__': main()