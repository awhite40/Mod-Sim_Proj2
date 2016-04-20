import simpy
import random

def refuel_aircraft(env, resource, name, aircraft_type):
    # Requsting
    # time_to_gate = 2
    # env.timeout(time_to_gate)
    request = resource.request()  # Generate a request event
    start = env.now
    print(name + "--> FUEL request a resource at %d" % start)
    yield request                 # Wait for access

    # Working
    print(name + "--> FUEL working on at %d" % env.now)

    unit_time_consuming = 2
    if aircraft_type == 20:
        working_duration = aircraft_type * (unit_time_consuming)
    else:
        working_duration = unit_time_consuming
    yield env.timeout(working_duration)          # Do something
    print(name + "--> FUEL done at %d" % env.now)
    # env.timeout(time_to_gate)
    # Releasing
    resource.release(request)     # Release the resource
    print(name + "--> FUEL finished refueling in %.1f minutes." % (env.now - start))


def water_aircraft(env, resource, name, type):
    # Requsting
    request = resource.request()  # Generate a request event
    start = env.now
    print(name + "--> WATER request a resource at %d" % start)
    yield request                 # Wait for access

    # Working
    print(name + "--> WATER working on at %d" % env.now)

    unit_time_consuming = 2
    if aircraft_type == 100:
        working_duration = aircraft_type * (unit_time_consuming)
    else:
        working_duration = unit_time_consuming
    yield env.timeout(working_duration)          # Do something
    print(name + "--> WATER done at %d" % env.now)

    # Releasing
    resource.release(request)     # Release the resource
    print(name + "--> WATER finished water supply in %.1f minutes." % (env.now - start))



# small type = 1, large tpye = 2, heavey type = 3
small_type = 2
large_type = 20

env = simpy.Environment()

res1 = simpy.PriorityResource(env, capacity=1)
res2 = simpy.PriorityResource(env, capacity=2)
# res3 = simpy.Resource(env, capacity=2)

# Generate aircraft here


aircraft1 = env.process(refuel_aircraft(env, res1, "A1", large_type))
# aircraft1 = env.process(water_aircraft(env, res2, "A1", small_type))

aircraft2 = env.process(refuel_aircraft(env, res1, "A2", small_type))
# aircraft2 = env.process(water_aircraft(env, res2, "A2", large_type))

# aircraft3 = env.process(refuel_aircraft(env, res1))
# aircraft3 = env.process(water_aircraft(env, res2))
env.run()


