for line in open("Terminal output test run"):
    words = line.split()
    #print words
    if words[:1] == Plane and words[:2] == 1:
        print words

