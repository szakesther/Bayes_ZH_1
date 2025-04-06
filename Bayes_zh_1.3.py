# Feladat 1.3 – Dobókockás (2 kocka, 4-est dobunk - mi a valószínűsége?)

import random

def kocka_dobas():
    return random.randint(1, 6) #ez egy kocka dobásának a szimulálása

def modell_ket_kocka_legalabb_4(futasok_szama=10000): # 10000 db dobást szimulálok
    kedvezo = 0 #számoljuk, háynszor jön ki olyan dobás, ahol az összess kisebb v egyenlő 4

    for i in range(futasok_szama): # itt megismételjük a dobásokat a megadott számban, vagyis 10.000szer
        k1 = kocka_dobas()
        k2 = kocka_dobas() # két dovkával dobunk
        osszeg = k1 + k2 #ezeknek az öszegét kiszámolom

        if osszeg >= 4: #ha legalább 4, akkor jó nekünk
            kedvezo += 1 # és ilyenkor a kedvezö dobások számát eggyel növeli

    valoszinuseg = kedvezo / futasok_szama #relatív gyakoriság kiszámolása, egy közelítő valószínűség
    print(f"Szimulációk száma: {futasok_szama}")
    print(f"Valószínűség, hogy összeg ≥ 4: {valoszinuseg:.4f}") #4 tizedesig kiírja

modell_ket_kocka_legalabb_4() #és már cska futtatjuk a modellt
