# Feladat 1.2 – Diszkalkuliás modell2 (megjegyzés: automatikusan 5-ször lefut)

import random

def complex_model_2():
    feature1 = ['könyvtáros', 'tanár']
    feature2 = ['csendes', 'cserfes']
    operator = ['és', 'vagy'] #itt a három lehteséges kategória (foglalkotás, személyiség és a logikai kapcsolo)

    word1 = random.choice(feature1)
    op = random.choice(operator)
    word2 = random.choice(feature2) # véletlenszerűen kiválasztjuk a mondat elemeit

    print(f"Premissza: Panni {word1} {op} {word2}.")#ez az eredeti premissza

    if op == 'és':#hogyan értelmezi a kapcsolatot? 95%ban és-t jól és 80%ban vagy-ot rosszul:
        értelmezett_op = 'és' if random.random() < 0.95 else 'vagy'
    else:
        értelmezett_op = 'és' if random.random() < 0.8 else 'vagy'

    print(f"(Íígy értelmezte: {értelmezett_op})")

    if értelmezett_op == 'és': # ha az értelmezés "és", mindkettő következik
        konklúzió1 = f"Panni {word1}."
        konklúzió2 = f"Panni {word2}."
        print("Konklúziók:")
        print("  -", konklúzió1)
        print("  -", konklúzió2)
        ervenyes = True
    else:
        print("Nem biztos a következtetés.")#vagy-ből nem vonhatunk biztos következtetést
        ervenyes = False

    print("Érvényes." if ervenyes else "Nem érvényes.")
    return ervenyes


# Ez is lefut 5ször

for i in range(5):
    print(f"\nFutás {i + 1}:")
    result = complex_model_2()
