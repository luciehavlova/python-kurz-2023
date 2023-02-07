import json

with open("body.json", encoding ="utf-8") as vstupni_soubor:
    data = json.load(vstupni_soubor)
    # data = vstupni_soubor.read()
            
# print(data)
# print(type(data))

for keys, values in (data.items()):
    # print(list(data.items()))

    if (data[keys])>= 60:
        data[keys] = "pass"
    else:
        data[keys] = "fail"

print(data)

# Ulozeni dat ze slovniku do souboru (zde do "out.json")
with open("out.json", mode="w", encoding="utf-8") as vystupni_soubor:
    json.dump(data, vystupni_soubor, ensure_ascii=False, indent=4)










