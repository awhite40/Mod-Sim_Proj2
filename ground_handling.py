# -*- coding: utf-8 -*-
# @Author: Jiahao
# @Date:   2016-04-13 10:21:41
# @Last Modified by:   Jiahao
# @Last Modified time: 2016-04-22 09:33:32

from RNG import *
import simpy
from random import seed, randint
import itertools
import numpy as np
import matplotlib.pyplot as plt

SMALL_SIZE = 1
LARGE_SIZE = 1.2
HEAVY_SIZE = 1.6


class aircraft(object):
    def __init__(self, env, name, size, gate, res1, res2, res3, res4, arrival_air):
        self.env = env
        self.name = name
        self.size = size
        self.gate = gate
        self.res1 = res1
        self.res2 = res2
        self.arrival_air = arrival_air
        # First Process - Request gate
        env.process(self.check_available_gate(env, name, size, gate, self.arrival_air))

    def check_available_gate(self, env, name, size, gate, arrival_air):
        # Wait for the time the plane is supposed to arrive
        yield env.timeout(arrival_air)
        print("%s requesting a gate at %.1f mins" %(self.name, env.now))
        request = gate.request()
        # Request one of the 11 gates
        yield request

        # Landing #
        arrival_time = env.now
        wait_time = 7  # wait time of 7 min applies for all aircrafts before processes can start - source Gantt chart in design doc
        # Determine the expected departure time a random time between 1 and 2 hours after the arrival at the gate
        departure_time = env.now + randint(60,120)
        num_of_processes = 0
        print("%s is landing at %.1f mins." % (self.name, arrival_time))
        # Wait for the plane to call for services after post-flight checks by pilots
        yield env.timeout(wait_time)
        
        # Begin processes for the different services
        yield env.process(self.refuel_aircraft(env, res1, name, size, arrival_time)) & env.process(self.water_aircraft(env, res2, name, size, arrival_time))
        & env.process(self.clean_aircraft(env, res3, name, size, arrival_time)) & env.process(self.cater_aircraft(env, res4, name, size, arrival_time))
        & env.process(self.power_aircraft(env, res5, name, size, arrival_time)) & env.process(self.baggage_aircraft(env, res6, name, size, arrival_time))
        # If the plane is on-time or late depart immediately
        if env.now >= departure_time:
            # Considered late if it leaves more than 15 mins after the planned departure
            if env.now > departure_time + 15:
                dif = env.now - deparure_time
                print (name + "is late by %.1f mins" %dif)
            else:
                print(name + "is on time")
            print("All process are done. " + name + " is departing at %.1f mins" %(env.now))
            yield env.timeout(2)
            # Release gate resource after 2 min changeover time
            gate.release(request)
        else: #Otherwise depart at scheduled departure time
            yield env.timeout(departure_time-env.now)
            print("%s is early" %(name))
            print("All process are done. " + name + " is departing at %.1f mins" %(env.now))
            yield env.timeout(2)
            gate.release(request)

    def refuel_aircraft(self, env, resource, name, size, arrival_time):
        # Requsting 
        #Define the disembark time
        disembark_time = 7
        #Introduce a prcess specific wait to account for disembarking for refuel process
        yield env.timeout(disembark_time)
        request = resource.request()  # Generate a request event
        start = env.now
        print(name + "--> FUEL request a resource at %.1f mins." % start)
        yield request                 # Wait for access
        # Working
        print(name + "--> FUEL working on at %.1f mins." % env.now)
        unit_time_consuming = 2
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE * (unit_time_consuming)
        elif size == LARGE_SIZE:
            working_duration = LARGE_SIZE * (unit_time_consuming)
        else:
            working_duration = HEAVY_SIZE * (unit_time_consuming)
        yield env.timeout(working_duration)          # Do something
        print(name + "--> FUEL done at %.1f mins." % env.now)

        # Releasing
        resource.release(request)     # Release the resource
        print(name + "--> FUEL finished refueling in %.1f mins." % (env.now - start))


    def water_aircraft(self, env, resource, name, size, arrival_time):
        # Requsting
        #Define the disembark time
        disembark_time = 7
        #Introduce a prcess specific wait to account for disembarking for water process
        yield env.timeout(disembark_time)
        request = resource.request()  # Generate a request event
        start = env.now
        print(name + "--> WATER request a resource at %.1f mins." % start)
        yield request                 # Wait for access

        # Working
        print(name + "--> WATER working on at %.1f mins." % env.now)
        unit_time_consuming = 3  #assuming larger volumes of water is filled
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE * (unit_time_consuming)
        elif size == LARGE_SIZE:
            working_duration = LARGE_SIZE * (unit_time_consuming)
        else:
            working_duration = HEAVY_SIZE * (unit_time_consuming)
        yield env.timeout(working_duration)          # Do something
        print(name + "--> WATER done at %.1f mins." % env.now)

        # Releasing
        resource.release(request)     # Release the resource
        print(name + "--> WATER finished water supply in %.1f mins." % (env.now - start))


    def clean_aircraft(self, env, resource, name, size, arrival_time):
        # Requsting
        #Define the disembark time
        disembark_time = 7
        #Introduce a prcess specific wait to account for disembarking for clean process
        yield env.timeout(disembark_time)
        request = resource.request()  # Generate a request event
        start = env.now
        print(name + "--> CLEAN request a resource at %.1f mins." % start)
        yield request                 # Wait for access

        # Working
        print(name + "--> CLEAN working on at %.1f mins." % env.now)
        unit_time_consuming = 4  # 4 is the value assumed for Clean
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE * (unit_time_consuming)
        elif size == LARGE_SIZE:
            working_duration = LARGE_SIZE * (unit_time_consuming)
        else:
            working_duration = HEAVY_SIZE * (unit_time_consuming)
        yield env.timeout(working_duration)          # Do something
        print(name + "--> CLEAN done at %.1f mins." % env.now)
        
        # Releasing
        resource.release(request)     # Release the resource
        print(name + "--> CLEAN finished water supply in %.1f mins." % (env.now - start))
        
    def cater_aircraft(self, env, resource, name, size, arrival_time):
        # Requsting
        #Define the disembark time
        disembark_time = 7
        #Introduce a prcess specific wait to account for disembarking for cater process
        yield env.timeout(disembark_time)
        request = resource.request()  # Generate a request event
        start = env.now
        print(name + "--> CATER request a resource at %.1f mins." % start)
        yield request                 # Wait for access

        # Working
        print(name + "--> CATER working on at %.1f mins." % env.now)
        unit_time_consuming = 5  # 5 is the value assumed for CATER
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE * (unit_time_consuming)
        elif size == LARGE_SIZE:
            working_duration = LARGE_SIZE * (unit_time_consuming)
        else:
            working_duration = HEAVY_SIZE * (unit_time_consuming)
        yield env.timeout(working_duration)          # Do something
        print(name + "--> CATER done at %.1f mins." % env.now)
        
        # Releasing
        resource.release(request)     # Release the resource
        print(name + "--> CATER finished process in %.1f mins." % (env.now - start))
        
        
    def power_aircraft(self, env, resource, name, size, arrival_time):
        # Requsting
        # do not use the disembark time since process can start earlier
        #disembark_time = 7
        request = resource.request()  # Generate a request event
        start = env.now
        print(name + "--> POWER request a resource at %.1f mins." % start)
        yield request                 # Wait for access

        #DO NOT use disembarking for power process since it can coexist
        #yield env.timeout(disembark_time)

        # Working
        print(name + "--> POWER working on at %.1f mins." % env.now)
        unit_time_consuming = 4
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE * (unit_time_consuming)
        elif size == LARGE_SIZE:
            working_duration = LARGE_SIZE * (unit_time_consuming)
        else:
            working_duration = HEAVY_SIZE * (unit_time_consuming)
        yield env.timeout(working_duration)          # Do something
        print(name + "--> POWER done at %.1f mins." % env.now)

        # Releasing
        resource.release(request)     # Release the resource
        print(name + "--> POWER finished charging in %.1f mins." % (env.now - start))   

# The Baggage process involves loading the aircaft with the departure passengers' luggages
    def baggage_aircraft(self, env, resource, name, size, arrival_time):
        # Requsting
        # do not use the disembark time since process can start earlier
        #disembark_time = 7
        request = resource.request()  # Generate a request event
        start = env.now
        print(name + "--> BAGGAGE request a resource at %.1f mins." % start)
        yield request                 # Wait for access

        #DO NOT use disembarking for power process since it can coexist
        #yield env.timeout(disembark_time)

        # Working
        print(name + "--> BAGGAGE working on at %.1f mins." % env.now)
        unit_time_consuming = 5
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE * (unit_time_consuming)
        elif size == LARGE_SIZE:
            working_duration = LARGE_SIZE * (unit_time_consuming)
        else:
            working_duration = HEAVY_SIZE * (unit_time_consuming)
        yield env.timeout(working_duration)          # Do something
        print(name + "--> BAGGAGE done at %.1f mins." % env.now)

        # Releasing
        resource.release(request)     # Release the resource
        print(name + "--> BAGGAGE finished charging in %.1f mins." % (env.now - start))   



#Initializing the environment
env = simpy.Environment()

# initializing the resources
gate = simpy.Resource(env, capacity=11)
res1 = simpy.PriorityResource(env, capacity=2)
res2 = simpy.PriorityResource(env, capacity=2)
res3 = simpy.PriorityResource(env, capacity=2)
res4 = simpy.PriorityResource(env, capacity=2)
#A1 = aircraft(env, '1', SMALL_SIZE, gate, res1, res2)
#A2 = aircraft(env, '2', LARGE_SIZE, gate, res1, res2)
#A3 = aircraft(env, '3', HEAVY_SIZE, gate, res1, res2)


#Creating a schedule of airplane arrivals
temp_schedule = []
generator = ClassRanGen()
for i in range(40):
    random_arrival_time = round(60*18 * generator.Rand(), 2)
    temp_schedule.append(random_arrival_time)
random_arrival_time = sorted(temp_schedule)
print(random_arrival_time)
k = 1

# Loop for generating aircraft according the the schedule above
for j in random_arrival_time:
    ID = 'Plane ' + str(k)
    s = randint(0,100)
    if s < 90:
        size = LARGE_SIZE
    elif s < 94:
        size = SMALL_SIZE
    else:
        size = HEAVY_SIZE
    arrival_air = j
    #print arrival_air
    craft = aircraft(env,ID,size,gate,res1,res2,res3, res4, arrival_air)
    k=k+1
# # Gaussian distribution
# mu, sigma = 0, 0.1 # mean and standard deviation
# s = np.random.normal(mu, sigma, 1000)
# x = mu + sigma*np.random.randn(10000)


# count, bins, ignored = plt.hist(s, 30, facecolor='cyan', normed=True)
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
#                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
#          linewidth=2, color='r')
# plt.show()

env.run()
