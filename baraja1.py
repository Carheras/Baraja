import random

_palos = ["o", "c", "e", "b"]
_cartas = ["As", "2", "3", "4", "5", "6", "7", "S", "C", "R"]

def baraja():

    result = []

    for palo in _palos:
        for carta in _cartas:
            result.append(carta + palo)
    return result

def elige_carta(i, longitud):
    return random.randint(0, longitud-1)

def mezclar(b):
    for i in range(len(b)):
        aux = b[i]
        al_azar = elige_carta(i, len(b))
        b[i] = b[al_azar]
        b[al_azar] = aux
    return b

print (mezclar(baraja()))







