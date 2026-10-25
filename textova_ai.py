import random

# Všetky vety, ktoré naša AI "prečíta" a naučí sa z nich
trenovacie_texty = [
    "umela inteligencia je buducnost technologii",
    "programovanie vo Visual Studio Code je velmi zabavne",
    "unity a blender pomahaju vytvarat krasne hry",
    "chcem vytvorit vlastnu aplikaciu za jeden tyzden",
    "python dokaze spracovat obrovske mnozstvo udajov",
    "kazdy den sa ucim nove veci o kodovani"
]

# Krok 1: Rozdelenie textu na slová
slova = []
for veta in trenovacie_texty:
    slova.extend(veta.split())

# Krok 2: Vytvorenie pamäte pre dvojice slov (pokročilejší kontext)
pamet_ai = {}
for i in range(len(slova) - 2):
    dvojica = (slova[i], slova[i + 1])
    nasledujuce = slova[i + 2]
    
    if dvojica not in pamet_ai:
        pamet_ai[dvojica] = []
    pamet_ai[dvojica].append(nasledujuce)

print("--- AI prečítala všetky texty a rozšírila svoju pamäť! ---")

# Krok 3: Generovanie odpovede na základe dvoch začiatočných slov
def generuj_odpoved(slovo1, slovo2, pocet_slov=5):
    aktualna_dvojica = (slovo1, slovo2)
    vysledok = [slovo1, slovo2]
    
    for _ in range(pocet_slov):
        if aktualna_dvojica in pamet_ai:
            dalsie = random.choice(pamet_ai[aktualna_dvojica])
            vysledok.append(dalsie)
            aktualna_dvojica = (aktualna_dvojica[1], dalsie)
        else:
            break
            
    return " ".join(vysledok)

# Vyskúšame našu múdrejšiu AI
vystup = generuj_odpoved("chcem", "vytvorit", pocet_slov=5)
print(f"\nZadal si: 'chcem vytvorit' -> AI hovorí: '{vystup}'")