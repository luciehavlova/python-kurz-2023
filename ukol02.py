sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input("Zadej kód součástky:")
if kod in sklad:
    print(f"Součastka s kódem {kod} je skladem v počtu {sklad[kod]} ks.")
    prodej = int(input("Zadej požadované množství:"))
    
    if (sklad[kod]) <= prodej:
      print(f"Součástka s kódem {kod} je pouze v omezeném množství.")
      sklad.pop(kod)

    elif (sklad[kod]) > prodej:
      print(f"Součástka je na skladě v dostatečném množství.")
      sklad[kod] = sklad[kod] - prodej
     
else:
  print("Součástka není na skladě.")




    

  
    


   
    # for p in sklad:
    # if prodej > sklad:
      # print ("Dostupné je jen omezené množství kusů.")
      # sklad.pop(kod)
    
    # else:
      # print("Poptávku lze uspokojit v plné výši.")
      # sklad = sklad - prodej



# else:
  # print("Součástka není skladem.")



# sales = 0
# for item in sklad:
  # sales += item["prodej"]
# print(f"Celkem bylo prodáno {sales} produktů")


    

