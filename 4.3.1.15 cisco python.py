from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
nm_fl= input("¿Cual es el nombre del archivo?: ")
try:
    file = open(nm_fl, "rt")
    for line in file:
        for ch in line:
            if ch.isalpha():
                counters[ch.lower()] += 1
    file.close()
    for ch in counters.keys():
        c = counters[ch]
        if c > 0:
            print(ch, '->', c)
except IOError:
    print("Error: ", strerror(IOError.errno))
