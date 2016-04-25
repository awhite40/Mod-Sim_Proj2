from RNG import *
import simpy
from random import seed, randint
import itertools
import numpy as np
import matplotlib.pyplot as plt

SMALL_SIZE=1
LARGE_SIZE=1.5
HEAVY_SIZE=2.5
SMALL_SIZE_constant = 0.7
SMALL_SIZE_Power_constant = 0.9

class aircraft(object):
    def __init__(self, env, name, size, gate, res1, res2, res3, res4, res5, res6, arrival_air_time, departure_time):
        self.env = env
        self.name = name
        self.size = size
        self.gate = gate
        #self.res1 = res1
        #self.res2 = res2
        #self.arrival_air_time = arrival_air_time
        #self.departure_time = departure_time
        env.process(self.check_available_gate(env, name, size, gate, arrival_air_time, departure_time))

    def check_available_gate(self, env, name, size, gate, arrival_air_time, departure_time):
        # Wait for the time the plane is supposed to arrive
        yield env.timeout(arrival_air_time)

        print("%s requesting a gate at %.1f minutes" %(self.name, env.now))
        request = gate.request()
        # Request one of the 11 gates
        yield request
        landing_time = 5
        
        yield env.timeout(landing_time)
        # Generate new aircrafts that arrive at the service hub. #
        arrival_time = env.now
        departure_time = env.now + float(randint(60, 120))
        print("%s is landing at %.1f minutes." % (self.name, arrival_time))

        wait_time = 7  # wait time of 7 min applies for all aircrafts before processes can start - source Gantt chart in design doc
        yield env.timeout(wait_time)
        yield env.process(self.refuel_aircraft(env, res1, name, size, arrival_time, departure_time)) & env.process(self.water_aircraft(env, res2, name, size, arrival_time, departure_time)) & env.process(self.clean_aircraft(env, res3, name, size, arrival_time, departure_time))& env.process(self.cater_aircraft(env, res4, name, size, arrival_time, departure_time)) & env.process(self.power_aircraft(env, res5, name, size, arrival_time, departure_time)) & env.process(self.baggage_aircraft(env, res6, name, size, arrival_time, departure_time))
        if env.now >= departure_time:
            if env.now > departure_time +15:
                print(name + " is late by %.1f minutes" % (env.now - departure_time))
            else:
                print(name + " is on time")
            print("All process are done. ")
            print(name + " is departing at %.1f minutes" % (env.now))
            yield env.timeout(2) # Aircraft is leaving the gate.
            gate.release(request)
        else:
            yield env.timeout(departure_time-env.now)
            print("%s is early" % (name))
            print("All process are done. ")
            print(name + " is departing at %.1f minutes" % (env.now))
            yield env.timeout(2) # Aircraft is leaving the gate.
            gate.release(request)

    def refuel_aircraft(self, env, resource, name, size, arrival_time, departure_time):
        # Requsting
        #Define the disembark time
        disembark_time = 7
        request = resource.request(priority=departure_time)  # Generate a request event
        
        print(name + " --> FUEL request a resource at %.1f minutes." % env.now)
        yield request                 # Wait for access
        start = env.now
        #Introduce a prcess specific wait to account for disembarking for refuel process
        yield env.timeout(disembark_time)

        # Working
        print(name + " --> FUEL working on at %.1f minutes." % env.now)
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE_constant* 17 #min
        elif size == LARGE_SIZE:
            working_duration = 17 #min
        else:
            working_duration = 28 #min
        yield env.timeout(working_duration)          # Do something
        print(name + " --> FUEL done at %.1f minutes." % env.now)
        end = env.now
        # Releasing
        resource.release(request)     # Release the resource
        print(name + " --> FUEL finished refueling in %.1f minutes." % (end - start))


    def water_aircraft(self, env, resource, name, size, arrival_time, departure_time):
        # Requsting
        #Define the disembark time
        disembark_time = 7
        request = resource.request(priority=departure_time)  # Generate a request event
        
        print(name + " --> WATER request a resource at %.1f minutes." % env.now)
        yield request                 # Wait for access
        start = env.now
        #Introduce a prcess specific wait to account for disembarking for supplying water process
        yield env.timeout(disembark_time)

        # Working
        print(name + " --> WATER working on at %.1f minutes." % env.now)
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE_constant* 11 #min
        elif size == LARGE_SIZE:
            working_duration = 11 #min
        else:
            working_duration = 14.5 #min
        yield env.timeout(working_duration)          # Do something
        print(name + " --> WATER done at %.1f mins." % env.now)
        end = env.now
        # Releasing
        resource.release(request)     # Release the resource
        print(name + " --> WATER finished supplying water in %.1f minutes." % (end - start))


    def clean_aircraft(self, env, resource, name, size, arrival_time, departure_time):
        # Requsting
        #Define the disembark time
        disembark_time = 7
        request = resource.request(priority=departure_time)  # Generate a request event
        
        print(name + " --> CLEAN request a resource at %.1f minutes." % env.now)
        yield request                 # Wait for access
        start = env.now
        #Introduce a specific wait to account for disembarking for cleaning process
        yield env.timeout(disembark_time)


        # Working
        print(name + " --> CLEAN working on at %.1f minutes." % env.now)
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE_constant* 11 #min
        elif size == LARGE_SIZE:
            working_duration = 11 #min
        else:
            working_duration = 29 #min
        yield env.timeout(working_duration)          # Do something
        print(name + " --> CLEAN done at %.1f mins." % env.now)
        end = env.now
        # Releasing
        resource.release(request)     # Release the resource
        print(name + " --> CLEAN finished cleaning in %.1f minutes." % (end - start))
        
    def cater_aircraft(self, env, resource, name, size, arrival_time, departure_time):
        # Requsting
        #Define the disembark time
        disembark_time = 7
        request = resource.request(priority=departure_time)  # Generate a request event
       
        print(name + " --> CATER request a resource at %.1f minutes." % env.now)
        yield request                 # Wait for access
        start = env.now
        #Introduce a process specific wait to account for disembarking for refuel process
        yield env.timeout(disembark_time)

        # Working
        print(name + " --> CATER working on at %.1f minutes." % env.now)
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE_constant* 15 #min
        elif size == LARGE_SIZE:
            working_duration = 15 #min
        else:
            working_duration = 30 #min
        yield env.timeout(working_duration)          # Do something
        print(name + " --> CATER done at %.1f minutes." % env.now)
        end = env.now
        # Releasing
        resource.release(request)     # Release the resource
        print(name + " --> CATER finished catering in %.1f minutes." % (end - start))

    

    def power_aircraft(self, env, resource, name, size, arrival_time, departure_time):
        # Requsting
        # do not use the disembark time since process can start earlier
        #disembark_time = 7
        request = resource.request(priority=departure_time)  # Generate a request event
        
        print(name + " --> POWER request a resource at %.1f minutes." % env.now)
        yield request                 # Wait for access

        #DO NOT use disembarking for power process since it can coexist
        #yield env.timeout(disembark_time)
        start = env.now
        # Working
        print(name + " --> POWER working on at %.1f minutes." % env.now)
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE_Power_constant* 44 #min
        elif size == LARGE_SIZE:
            working_duration = 44 #min
        else:
            working_duration = 54 #min
        yield env.timeout(working_duration)          # Do something
        print(name + " --> POWER done at %.1f minutes." % env.now)
        resource.release(request)
        print(name + " --> POWER finished charging in %.1f minutes." % (env.now - start))
        
    # PROCESS Baggage involves loading the baggage of future passengers (departure) only    
    def baggage_aircraft(self, env, resource, name, size, arrival_time, departure_time):
        # Requsting
        # do not use the disembark time since process can start earlier
        #disembark_time = 7
        request = resource.request(priority=departure_time)  # Generate a request event
        
        print(name + " --> BAGGAGE request a resource at %.1f minutes." % env.now)
        yield request                 # Wait for access

        #DO NOT use disembarking for power process since it can coexist
        #yield env.timeout(disembark_time)
        start = env.now
        # Working
        print(name + " --> BAGGAGE working on at %.1f minutes." % env.now)
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE_constant*16 #min
        elif size == LARGE_SIZE:
            working_duration = 16 #min
        else:
            working_duration = 28 #min
        yield env.timeout(working_duration)          # Do something
        print(name + " --> BAGGAGE done at %.1f minutes." % env.now)
 
        # Releasing
        resource.release(request)     # Release the resource
        print(name + " --> BAGGAGE finished loading in %.1f minutes." % (env.now - start))




env = simpy.Environment()




gate = simpy.Resource(env, capacity=11)
res1 = simpy.PriorityResource(env, capacity=3)
res2 = simpy.PriorityResource(env, capacity=3)
res3 = simpy.PriorityResource(env, capacity=3)
res4 = simpy.PriorityResource(env, capacity=3)
res5 = simpy.PriorityResource(env, capacity=3)
res6 = simpy.PriorityResource(env, capacity=3)
#A1 = aircraft(env, '1', SMALL_SIZE, gate, res1, res2)
#A2 = aircraft(env, '2', LARGE_SIZE, gate, res1, res2)
#A3 = aircraft(env, '3', HEAVY_SIZE, gate, res1, res2)



arrive_depart_schedule = []
generator = ClassRanGen()
for i in range(40):
    random_arrival_time = round(60*18 * generator.Rand(), 2)
    random_departure_time = random_arrival_time + float(randint(60, 120))
    arrive_depart_schedule.append([random_arrival_time, random_departure_time])

arrive_depart_schedule = sorted(arrive_depart_schedule)
#print(arrive_depart_schedule)

k = 1
count_small = 0
count_heavy = 0
for j in range(len(arrive_depart_schedule)):
    ID = 'Plane ' + str(k)

    # size distribution
    s = randint(0,100)
    if s < 90:
        size = LARGE_SIZE
    
    elif s <94:
        size = SMALL_SIZE
        count_small = count_small +1
    else:
        size = HEAVY_SIZE
        count_heavy = count_heavy +1
    arrival_air_time = arrive_depart_schedule[j][0]
    departure_time = arrive_depart_schedule[j][1]
    #print arrival_air
    craft = aircraft(env, ID, size, gate, res1, res2, res3, res4, res5, res6, arrival_air_time, departure_time)
    k = k + 1
print 'Heavy Planes', count_heavy, 'Small Planes', count_small


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
