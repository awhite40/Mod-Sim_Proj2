#for x in rang
Planes = [dict() for x in range(40)]
#print Planes2
#Plane1 = dict([('Arrival', 0)])
for line in open("Terminal output test run"):
    words = line.split()
    for x in range(40):
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
#print Planes[x], x
Arrival=[0]*40
Departing = [0]*40
Difference = [0]*40
print Planes[1]
for x in range(40):
    print x
    Arrival[x] = float(Planes[x]['Arrival'])
    Departing[x] = float(Planes[x]['Depart'])
    Difference[x] = Departing[x] - Arrival[x]
print 'Arrival', Arrival#, 'Departure', Depart, 'Time between arrival and departure', Difference