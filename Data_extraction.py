
Plane1 = dict([('Arrival', 0)])
for line in open("Terminal output test run"):
    words = line.split()
    #print words
    #break
    if (words[0] == 'Plane' and words[1] == '1'):
        if (words[3] == 'POWER' and words[4] == 'done'):
            Plane1['POWER'] = words[6]
        if (words[3] == 'BAGGAGE' and words[4] == 'done'):
            Plane1['BAGGAGE'] = words[6]
        if (words[3] == 'FUEL' and words[4] == 'done'):
            Plane1['FUEL'] = words[6]
        if (words[3] == 'CLEAN' and words[4] == 'done'):
            Plane1['CLEAN'] = words[6]
        if (words[3] == 'landing'):
            Plane1['LANDING'] = words[5]
        if (words[2] == 'requesting' and words[4] == 'gate'):
            Plane1['Arrival'] = words[6]
        if (words[3] == 'CATER' and words[4] == 'done'):
            Plane1['CATER'] = words[6]
        #print words
print Plane1