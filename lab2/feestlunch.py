#prijzen van producten
print("----------------------------------------------------")
prijscroissant = input("| Prijs Croissant    :")           
prijsstokbrood = input("| Prijs Stokbrood    :")           
waardekorting  = input("| Kortingsbon Waarde :")           
aantcroissant  = input("| Aantal Croissantjes:")           
aantstokbrood  = input("| Aantal Stokbrood   :")           
aantkorting    = input("| Aantal Kortingsbon :")           
print("----------------------------------------------------")


# print(aantcroissant * prijscroissant + aantstokbrood * prijsstokbrood - aantkorting * waardekorting)
prijs = float(aantcroissant) * float(prijscroissant) + float(aantstokbrood) * float(prijsstokbrood) - float(aantkorting) * float(waardekorting)

print("De feestlunch kost je bij de bakker " + str(prijs) + " euro voor de " + str(aantcroissant) + " croissantjes en de " + str(aantstokbrood) + " stokbroden als de " + str(aantkorting) + " kortingsbonnen nog geldig zijn!")