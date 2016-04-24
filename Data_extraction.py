
import cPickle as pickle
#for x in rang
Num_planes = 40
num_runs = 14

for num in range(num_runs):
    Planes = [dict() for x in range(Num_planes)]
    #print Planes2
    #Plane1 = dict([('Arrival', 0)])
    for line in open('Data Outputs/Run' + str(num+1)):
        words = line.split()
        for x in range(Num_planes):
            if (words[0] == 'Plane' and words[1] == str(x+1)):
                #print words
                if (words[3] == 'POWER' and words[4] == 'done'):
                    Planes[x]['POWER'] = words[6]
                if (words[3] == 'BAGGAGE' and words[4] == 'done'):
                    Planes[x]['BAGGAGE'] = words[6]
                if (words[3] == 'FUEL' and words[4] == 'done'):
                    Planes[x]['FUEL'] = words[6]
                if (words[3] == 'CLEAN' and words[4] == 'done'):
                    Planes[x]['CLEAN'] = words[6]
                if (words[3] == 'landing'):
                    Planes[x]['LANDING'] = words[5]
                if (words[2] == 'requesting' and words[4] == 'gate'):
                    Planes[x]['Arrival'] = words[6]
                if (words[3] == 'CATER' and words[4] == 'done'):
                    Planes[x]['CATER'] = words[6]
                if (words[3] == 'departing'):
                    Planes[x]['Depart'] = words[5]
                if (words[3] =='WATER' and words[4]):
                    Planes[x]['WATER'] = words[6]
            if words[
    #print Planes[x], x
    Arrival=[0]*Num_planes
    Depart = [0]*Num_planes
    Difference = [0]*Num_planes
#print Planes[1]
    for x in range(Num_planes):
        #print x
        Arrival[x] = float(Planes[x]['Arrival'])
        Depart[x] = float(Planes[x]['Depart'])
        Difference[x] = Depart[x] - Arrival[x]
    avg_time = sum(Difference)/Num_planes
    print avg_time

#print 'Arrival', Arrival#, 'Departure', Depart, 'Time between arrival and departure', Difference
#pickle.dump((Planes,Arrival,Depart,Difference), open('Run'+str(num+1) + '.pkl', 'wb'))