class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
    
    def pujc_auto(self):
        self.dostupne = False

    def __str__(self):
        if self.dostupne: 
            stav = "Potvrzuji zapůjčení vozidla."
        else:
            stav = "Vozidlo není k dispozici."
        return f"dosupnost: {stav}"
    
    def get_info(self):
        return f"Vozidlo {self.registracni_znacka}, typ {self.typ_vozidla}."

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

typ = ["peugeot", "skoda"]
typ = input("Zadejte typ auta, který si chcete půjčit:")
if typ == "peugeot":
    print(peugeot.get_info())
    peugeot.pujc_auto() 
    print(peugeot)   
    # peugeot.pop
elif typ == "skoda":
    print(skoda.get_info())
    print(skoda)
    # typ.pop(skoda)
else:
    print("Tento typ není k dispozici")

# print(peugeot)
# print(skoda.get_info())
# skoda.pujc_auto()
# print(skoda)
