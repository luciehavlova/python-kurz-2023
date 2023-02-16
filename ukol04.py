
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