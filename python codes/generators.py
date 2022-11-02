def generator():
    n = 1
    print ("this is the first generation of a generator")
    yield n
    n = 2
    print  ("this is the second generation of the system")
    yield n 
    n = 3
    print ("this isthe 3rd generation of the system")
    yield n
for item in  generator():
    print(item)