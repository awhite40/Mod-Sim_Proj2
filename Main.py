import random
import sys
import simpy

from ServiceHub import ServiceHub as sh
from Aircraft import Aircraft as ac

# ================Setup================

RANDOM_SEED = 42
NUM_TRUCKS1 = 2             # Number of trucks for cleaning in the servicehub
NUM_TRUCKS2 = 2             # Number of trucks for water supply in the servicehub
NUM_TRUCKS3 = 2             # Number of trucks for power supply in the servicehub
CLEANTIME = 10              # Minutes it takes to clean an aircraft
WATERTIME = 10              # Minutes it takes to supply water to an aircraft
POWERTIME = 10              # Minutes it takes to power up an aircraft
SIM_TIME = 120              # Simulation time in minutes
T_INTER = [30, 300]         # Create an aircraft every [min, max] mins
Gate_1_A = True
Gate_2_A = True
Gate_3_A = True

# class Main(object):
#     def __init__(self, env, num_trucks1, num_trucks2, num_trucks3, cleantime, watertime, powertime):
#         self.env = env
#         self.name = name
#         self.size = size



def aircraft_generator(env, service_hub, fuel_pump):
    
    if Gate_1_free == True:
        Plane_Gate = 'Gate 1'
        Gate_1_free = False
        comm.Send(Plane_Gate, dest = 1)  # Schedule services
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
        #Add plane to queue'''
    """Generate new aircrafts that arrive at the service hub."""
    for i in itertools.count():
        yield env.timeout(random.randint(*T_INTER))
        env.process(aircraft('Aircraft %d' % i, env, service_hub, fuel_pump))

# Setup and start the simulation
print('Aircraft Service Ground Handling')
random.seed(RANDOM_SEED)  # This helps reproducing the results

# Create an environment and start the setup process
env = simpy.Environment()
# Create the servicehub
service_hub = sh(env, 2, 10)
# Create one aircraft
aircraft = ac(env, "A1", 1)
while env.now < SIM_TIME - 60
    arrival_time = env.now
    Gate, Departure_time, Plane_ID = env.process(aircraft_generator(env, ID, arrival_time, gate))
env.process(gas_station_control(env, fuel_pump))
env.process(aircraft_generator(env, gas_station, fuel_pump))

env.run(until=500)


# if __name__ == '__main__': Main()
