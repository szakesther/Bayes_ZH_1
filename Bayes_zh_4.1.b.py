import random

szinek = [1, 2, 3, 4] #1=kör,2=káró,3=treff,4=pikk
figurak = [1, 2, 3, 4] #1=jumbo,2=dáma,3=király,4=ász

pakli = [(s, f) for s in szinek for f in figurak] #figurás pakli: 16 lap

def szimulacio(n=100000):
    osszes_Y_pikk_dama = 0
    kedvezo_eset = 0

    for _ in range(n):
        lapok = random.sample(pakli, 2)  #két különböző lap
        X, Y = lapok[0], lapok[1]

        if Y == (4, 2): # sak azokat az eseteket nézzük, ahol Y = pikk dáma
            osszes_Y_pikk_dama += 1

            if X == (3, 3) or X == (3, 4): #ha X treff király vagy treff ász
                kedvezo_eset += 1

    if osszes_Y_pikk_dama == 0:
        print("Nem volt Y = pikk dáma az adatok között!")
    else:
        valoszinuseg = kedvezo_eset / osszes_Y_pikk_dama
        print(f"P(X = treff király vagy ász | Y = pikk dáma) ≈ {valoszinuseg:.4f}")

szimulacio() #futi
