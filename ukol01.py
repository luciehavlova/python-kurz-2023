jmeno = ["Lucie"]
for j in jmeno:
    mail = j + "@czechitas.cz"
    print (mail)

jmeno_a_prijmeni = input("Napiš jméno a příjmení:")
print(jmeno_a_prijmeni)

print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
print(jmeno_a_prijmeni.title()) #první písmeno velké a další malá
# nebo rozděli pomocí indexace a slicingu
jmeno = jmeno_a_prijmeni.split()[0]
prijmeni = jmeno_a_prijmeni.split()[1]
# Můžeme využít f-string (formátovaný řetězec)
print(f'{jmeno[0].upper()}{jmeno[1:].lower()} {prijmeni[0].upper()}{prijmeni[1:].lower()}')
# nebo klasicky spojit řetězce pomocí +
print(jmeno[0].upper() + jmeno[1:].lower() + " " + prijmeni[0].upper() + prijmeni[1:].lower())


# Můžeme využít f-string (formátovaný řetězec) - iniciály s tečkou
print(f"{jmeno[0].upper()}. {prijmeni[0].upper()}.")

if len(jmeno) > 5:
    print(f"{jmeno[0].upper()}. {prijmeni.title()}")
    # Pripadne:
    print(f"{jmeno[0].upper()}. {prijmeni.capitalize()}")
else:
    print(jmeno_a_prijmeni.titlem())






jmeno = "Anna"

# Můžeme využít f-string (formátovaný řetězec)
print(f"{jmeno}@czechitas.cz")
# nebo klasicky spojit řetězce pomocí +
print(jmeno + "@czechitas.cz")