# 3.2 – X,Y,Z

import random
from collections import Counter

def valtozo():
    return random.choice([0, 1, 2, 3]) #egyenletes eloszlással választ egy értéket

def model_X(szimulaciok_szama=100000): #ez a modeel: ha tudjuk, hogy W=X+Y+Z, akkor mennyi a valószínűsége X különböző értékeinek?
    eredmenyek = []

    for _ in range(szimulaciok_szama):
        X = valtozo()
        Y = valtozo()
        Z = valtozo()
        W = X + Y + Z

        if W == 7: #csak ezt az esetet vizsgáljuk
            eredmenyek.append(X)

    gyakorisag = Counter(eredmenyek)  #hányszor fordult elő egy-egy érték (0, 1, 2, 3)
    osszes = sum(gyakorisag.values())

    for ertek in range(4):  # X csak 0,1,2,3 lehet
            db = gyakorisag.get(ertek, 0)  #ha egy érték nem szerepelt, akkor 0-nak tekintjük
            valoszinuseg = db / osszes if osszes > 0 else 0
            print(f"X = {ertek} → {valoszinuseg:.4f}")
model_X() #futi
#megjegyzés:  = 0 sosem fordul elő, mert ha X = 0, Y+Z maximum 6 lehet
