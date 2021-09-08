#Lukas van Hulst 
#opdracht: Pizza calculator
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|Voer in hoeveel je van elke soort wilt")

#input voor hoeveelheid pizza's
Spizza = int(input("|Small Pizza's :"))
Mpizza = int(input("|Medium Pizza's:"))
Lpizza = int(input("|Large Pizza's :"))

#prijzen van pizza's
Psmall   = 5.99
Pmedium  = 7.99
Plarge   = 11.99

#prijs bereken
totaal = Spizza * Psmall + Mpizza * Pmedium + Lpizza * Plarge 

#overzicht van bestelling
print("U heeft een bestelling gemaakt van " + str(totaal) + " voor " + str(Spizza) + " small pizza's, " + str(Mpizza) + " medium pizza's en " + str(Lpizza) + " large pizza")