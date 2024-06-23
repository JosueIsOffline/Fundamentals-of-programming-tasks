def counter(str):
    return print(len(str))

counter("Hola")


def counter2(str):
    x = 0
    for i in str:
        x += 1 
        
    print(x)


counter2("Platano maduro")