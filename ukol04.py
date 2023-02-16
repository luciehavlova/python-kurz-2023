
def zasilani_sms(overeni_cisla):
    cislo = int(overeni_cisla[:4])
    if cislo == "+420":
        return cislo
    else:
        print("Chybné číslo")
        exit()
cislo = int(input("Zadej telefonní číslo s předvolbou:"))



def cena_zpravy(zprava):
    pocet_znaku = len(zprava)
    print(len(zprava))
    zprava = round(int(pocet_znaku * 3 / 180))
    
zprava = input("Zadej textovou zprávu:")

# print (f"Cena za odeslání SMS na číslo {telefonni_cislo} je {cena_zpravy} Kč.")

# opravená varianta:
cislo = input("Zadej telefonní číslo s předvolbou:")

def zasilani_sms(overeni_cisla)->int:
    return len (overeni_cisla)==9 or (len(overeni_cisla)==12 and overeni_cisla[:4]=="+420")

zprava = input("Zadej textovou zprávu:")

def cena_zpravy(cena):
    return cena 
cena = len(zprava) * 3 /180

 
print (f"Cena za odeslání SMS na číslo {cislo} je {cena} Kč.")