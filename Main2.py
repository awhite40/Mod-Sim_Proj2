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
class Plane(object):
    def __init__(self,env):
        self.env = env
        self.action = env.process(self.run())
    def run(self):
        while True:
            print interarrival_time, env.now
            yield self.env.timeout(interarrival_time)
            self.arrival_time = self.env.now
            print("Created Airplane")
            if Gate_1_A == True:
                self.Plane_Gate = 'Gate 1'
                Gate_1_free = False
        
            elif Gate_2_A == True:
                self.Plane_Gate = 'Gate 2'
                Gate_2_free = False
            #comm.Send(Plane_Gate, dest=1)  # Schedule first service
            elif Gate_3_A == True:
                self.Plane_Gate = 'Gate 3'
                Gate_3_free = False
            #comm.Send(Plane_Gate, dest=1)  # Schedule first service
             # Schedule first service
            else:
                plane_queue = plane_queue + 1
                self.Plane_Gate = 'Queue'

# Setup and start the simulation
print('Aircraft Service Ground Handling')
random.seed(RANDOM_SEED)  # This helps reproducing the results

# Create an environment and start the setup process
env = simpy.Environment()
# Create the servicehub
service_hub = sh(env, 2, 10)
# Create one aircraft
aircraft = ac(env, "A1", 1)
i = 100

print env.now
while i < 500 :
    arrival_time = env.now
    interarrival_time = 35 + random.randint(0,60)
    Planes= Plane(env)
    i = i+ interarrival_time
    print i
#env.process(gas_station_control(env, fuel_pump))
#env.process(aircraft_generator(env, gas_station, fuel_pump))

env.run(until=500)
print(Planes)

# if __name__ == '__main__': Main()
