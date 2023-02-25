import re
regularni_vyraz = re.compile(r"([a-z]|[A-Z]){6,10}")
jmeno = input("Zadej uživatelské jméno:")
hledani = regularni_vyraz.fullmatch(jmeno)
if hledani:
    print("Uživatelské jméno je v pořádku")
else:
    print("Uživatelské jméno není v pořádku")
    exit()

import re
regularni_vyraz = re.compile(r"([a-z]|[A-Z]|[0-9]|\_|\+|\.|\-|\=){12,30}")
heslo = input("Zadej heslo:")
kontrola = regularni_vyraz.fullmatch(heslo)
if kontrola:
    print("Heslo je v pořádku")
else:
    print("Špatné heslo")
    exit()

regularni_vyraz = re.compile(r"\"?\w+(\.|\+|\-)?\w+\"?\@\[?\w+(\.|\-)?\w+?\.?\w+?\.?\w+\.?\w+\.?\w+\]?\\?")
email = input("Zadej e-mail:")
control = regularni_vyraz.fullmatch(email)
if control:
    print("Email je v pořádku")
else:
    print("Email není v pořádku")
    exit()

