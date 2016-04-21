"""
CSE6730 Project 2- team 12
"""


import simpy
import random
import itertools

SMALL_SIZE = 1
LARGE_SIZE = 1.2
HEAVY_SIZE = 1.6

class aircraft(object):
    def __init__(self, env, name, size, gate, res1, res2, human):
        self.env = env
        self.name = name
        self.size = size
        self.gate = gate
        self.res1 = res1
        self.res2 = res2
        self.human = human

        env.process(self.check_available_gate(env, name, size, gate))

    def check_available_gate(self, env, name, size, gate):
        request = gate.request()
        # Request one of the 11 gates
        yield request

        # Generate new aircrafts that arrive at the service hub. #
        arrival_time = env.now
        #Defining the process_suit_time = arrival time + wait time of 7 min + disembarking time 8 min
        process_suit_time = arrival_time + 900
        #Defining the bag_pow_time = arrival time + wait time of 7 min 
        bag_pow_time = arrival_time + 420
        num_of_processes = 0
        print("%s is landing at %.1f mins." % (self.name, arrival_time))
        yield env.timeout(10)
        env.process(self.refuel_aircraft(env, res1, name, size, arrival_time))
        env.process(self.water_aircraft(env, res2, name, size, arrival_time))
        #check that call time = arrival time + wait time = process_suit_time
        env.process(self.catering_aircraft(env, res2, name, size, process_suit_time))
        # print("All process are done. " + name + " is departing now")
        gate.release(request)

    def refuel_aircraft(self, env, resource, name, size, arrival_time,):
        # Requsting
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
        else size == HEAVY_SIZE:
            working_duration = HEAVY_SIZE * (unit_time_consuming)
        yield env.timeout(working_duration)          # Do something
        print(name + "--> FUEL done at %.1f mins." % env.now)
        # env.timeout(time_to_gate)
        # Releasing
        resource.release(request)     # Release the resource
        print(name + "--> FUEL finished refueling in %.1f mins." % (env.now - start))
        return 1

    def water_aircraft(self, env, resource, name, size, arrival_time):
        # Requsting
        request = resource.request()  # Generate a request event
        start = env.now
        print(name + "--> WATER request a resource at %.1f mins." % start)
        yield request                 # Wait for access

        # Working
        print(name + "--> WATER working on at %.1f mins." % env.now)

        unit_time_consuming = 2
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE * (unit_time_consuming)
        elif size == LARGE_SIZE:
            working_duration = LARGE_SIZE * (unit_time_consuming)
        else size == HEAVY_SIZE:
            working_duration = HEAVY_SIZE * (unit_time_consuming)
        yield env.timeout(working_duration)          # Do something
        print(name + "--> WATER done at %.1f mins." % env.now)
        return 1

        # Releasing
        resource.release(request)     # Release the resource
        print(name + "--> WATER finished water supply in %.1f mins." % (env.now - start))

    def clean_aircraft(self, env, resource, human, name, size, arrival_time):
        # Requsting
        request = resource.request()
        request = human.request()# Generate a request event
        start = env.now
        print(name + "--> CLEAN request a resource at %.1f mins." % start)
        yield request                 # Wait for access

        # Working
        print(name + "--> CLEAN working on at %.1f mins." % env.now)

        unit_time_consuming = 2
       if size == SMALL_SIZE:
            working_duration = SMALL_SIZE * (unit_time_consuming)
        elif size == LARGE_SIZE:
            working_duration = LARGE_SIZE * (unit_time_consuming)
        else size == HEAVY_SIZE:
            working_duration = HEAVY_SIZE * (unit_time_consuming)
        print(name + "--> CLEAN done at %.1f mins." % env.now)
        return 1

        # Releasing
        resource.release(request)     # Release the resource
        print(name + "--> CLEAN finished cleaning in %.1f mins." % (env.now - start))


        #Code for Catering - Sumana start
        def catering_aircraft(self, env, resource, name, size, process_suit_time,):
        # Requsting
        request = resource.request()  # Generate a request event
        start = env.now
        print(name + "--> Catering request a resource at %.1f mins." % start)
        yield request                 # Wait for access

        # Working
        print(name + "--> Catering working on at %.1f mins." % env.now)
        unit_time_consuming = 2
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE * (unit_time_consuming)
        elif size == LARGE_SIZE:
            working_duration = LARGE_SIZE * (unit_time_consuming)
        else size == HEAVY_SIZE:
            working_duration = HEAVY_SIZE * (unit_time_consuming)
        yield env.timeout(working_duration)          # Do something
        print(name + "--> Catering done at %.1f mins." % env.now)
        # env.timeout(time_to_gate)
        # Releasing
        resource.release(request)     # Release the resource
        print(name + "--> Catering finished refueling in %.1f mins." % (env.now - start))
        return 1


        #Code for Power - Sumana start - Power process can start earlier, 7 mins after gate arrival
        def Power_aircraft(self, env, resource, name, size, bag_pow_time,):
        # Requsting
        request = resource.request()  # Generate a request event
        start = env.now
        print(name + "--> Power request a resource at %.1f mins." % start)
        yield request                 # Wait for access

        # Working
        print(name + "--> Power working on at %.1f mins." % env.now)
        unit_time_consuming = 2
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE * (unit_time_consuming)
        elif size == LARGE_SIZE:
            working_duration = LARGE_SIZE * (unit_time_consuming)
        else size == HEAVY_SIZE:
            working_duration = HEAVY_SIZE * (unit_time_consuming)
        yield env.timeout(working_duration)          # Do something
        print(name + "--> Power done at %.1f mins." % env.now)
        # env.timeout(time_to_gate)
        # Releasing
        resource.release(request)     # Release the resource
        print(name + "--> Power finished refueling in %.1f mins." % (env.now - start))
        return 1

        #Code for Baggage out - Sumana start - Baggage process can start earlier, 7 mins after gate arrival
        def baggage_out_aircraft(self, env, resource, name, size, bag_pow_time,):
        # Requsting
        request = resource.request()  # Generate a request event
        start = env.now
        print(name + "--> Baggage Out request a resource at %.1f mins." % start)
        yield request                 # Wait for access

        # Working
        print(name + "--> Baggage Out working on at %.1f mins." % env.now)
        unit_time_consuming = 2
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE * (unit_time_consuming)
        elif size == LARGE_SIZE:
            working_duration = LARGE_SIZE * (unit_time_consuming)
        else size == HEAVY_SIZE:
            working_duration = HEAVY_SIZE * (unit_time_consuming)
        yield env.timeout(working_duration)          # Do something
        print(name + "--> Baggage Out done at %.1f mins." % env.now)
        # env.timeout(time_to_gate)
        # Releasing
        resource.release(request)     # Release the resource
        print(name + "--> Baggage Out finished refueling in %.1f mins." % (env.now - start))
        return 1

        #Code for Baggage Load - Sumana start - Baggage load starts later , after baggage out process is completed
        def baggage_load_aircraft(self, env, resource, name, size, arrival_time,):
        # Requsting
        request = resource.request()  # Generate a request event
        start = env.now
        print(name + "--> Baggage Load request a resource at %.1f mins." % start)
        yield request                 # Wait for access

        # Working
        print(name + "--> Baggage Load working on at %.1f mins." % env.now)
        unit_time_consuming = 2
        if size == SMALL_SIZE:
            working_duration = SMALL_SIZE * (unit_time_consuming)
        elif size == LARGE_SIZE:
            working_duration = LARGE_SIZE * (unit_time_consuming)
        else size == HEAVY_SIZE:
            working_duration = HEAVY_SIZE * (unit_time_consuming)
        yield env.timeout(working_duration)          # Do something
        print(name + "--> Baggage Load done at %.1f mins." % env.now)
        # env.timeout(time_to_gate)
        # Releasing
        resource.release(request)     # Release the resource
        print(name + "--> Baggage Load finished refueling in %.1f mins." % (env.now - start))
        return 1







env = simpy.Environment()
gate = simpy.Resource(env, capacity=1)
res1 = simpy.PriorityResource(env, capacity=1)
res2 = simpy.PriorityResource(env, capacity=2)
human = simpy.Resource(env, capacity=1)
A1 = aircraft(env, '1', SMALL_SIZE, gate, res1, res2, human)
A2 = aircraft(env, '2', LARGE_SIZE, gate, res1, res2, human)
A3 = aircraft(env, '3', HEAVY_SIZE, gate, res1, res2, human)
env.run()
