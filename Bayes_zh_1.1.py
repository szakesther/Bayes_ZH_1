# Feladat 1.1 – Diszkalkuliás modell (megjegyzés: automatikusan 5-ször lefut)

import random

def complex_model_1():
    feature1 = ['könyvtáros', 'tanár']
    feature2 = ['csendes', 'cserfes']
    operator = ['és', 'vagy'] #itt a három lehteséges kategória (foglalkotás, személyiség és a logikai kapcsolo)

    word1 = random.choice(feature1)
    op = random.choice(operator)
    word2 = random.choice(feature2) # véletlenszerűen kiválasztjuk a mondat elemeit

    # 20% eséllyel felcseréljük a szót (diszlexiás csere)
    if random.random() < 0.2:
        print("Diszlexiás csere!") # hogy aki lefutattja lássa, melyik esetben történik meg
        word3 = 'csendes' if word2 == 'cserfes' else 'cserfes' #felcserélem a szavakat csendes-cserfes
    else:
        word3 = word2 #ha nem történik meg a diszes csere, ua. a szó következik

    print(f"Premissza: Panni {word1} {op} {word2}.")
    print(f"Konklúzió: Panni {word3}.") #kiírjuk őket

    if op == 'és': #logikai érvényesség eldöntése: ha és, akkor érvényes a következtetés, ha vagy, akkor nem érvényes
        ervenyes = word2 == word3
    else:
        ervenyes = False

    print("Érvényes." if ervenyes else "Nem érvényes.") #ezt a következtetés ki is írjuk
    return ervenyes

# nem tetszett, hogy folyton le kellett futattni, így inkább lefuttatom ötször, és valószínüleg ki fog jönni a diszes verzió is

for i in range(5):
    print(f"\nFutás {i + 1}:")
    result = complex_model_1()
