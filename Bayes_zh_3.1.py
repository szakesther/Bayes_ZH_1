# 3.1 – két húzott lapból egyik király, másik nem

import random

def kartyahuzas():
    pakli = ['K'] * 4 + ['N'] * 48 # 52 lap: 4 Király, 48 Nem
    huzott = random.sample(pakli, 2)  #húzunk két lapot
    return huzott

def model_kiraly(szimulacio_szama=100000):
    kedvezo = 0

    for _ in range(szimulacio_szama):
        lapok = kartyahuzas()

        if 'K' in lapok and 'N' in lapok: #a Király kedvező lap, hozzáadjuk
            kedvezo += 1

    valoszinuseg = (kedvezo*2) / szimulacio_szama #megszorzom kettővel, mert amikor mind a kettő lap király, azt csak egyszer számolná
    print(f"Szimulációk: {szimulacio_szama}")
    print(f"Valószínűség (egyik K, másik nem): {valoszinuseg:.4f}")

# Futtatás
model_kiraly()
