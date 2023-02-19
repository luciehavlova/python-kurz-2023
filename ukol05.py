teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# a:
prumer = [sum(cisla)/len(cisla) for cisla in teploty]
print(prumer)
# b:
ranni_teploty = [ranni[0] for ranni in teploty]
print(ranni_teploty)
# c:
nocni_teploty = [nocni[2] for nocni in teploty]
print(nocni_teploty)
# d:
poledni_nocni_teploty = [[poledni[1], poledni[3]] for poledni in teploty]
print(poledni_nocni_teploty)

# bonus:
teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

# prumer = {den: f"{sum(teploty[den])/len(teploty[den])}" for den in teploty}
# print(prumer)


