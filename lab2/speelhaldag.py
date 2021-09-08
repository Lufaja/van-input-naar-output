print("------------------------------------------------------------------------------------")
personen      = int(input("| Aantal Personen                      :")) 
prijskaart    = float(input("| Prijs Kaartje                        :")) 
VRprijs       = float(input("| Prijs van VR                         :")) 
VRtijdpersoon = int(input("| Hoelang VR(stappen van 5 minuten)    :")) 
print("------------------------------------------------------------------------------------")


# personen      = 4
# prijskaart    = 7.45
# VRprijs       = 0.37 #per 5 minuten
# VRtijdpersoon = 45
VRtotaaltijd  = personen * VRtijdpersoon

# print(personen * prijskaart + VRtotaaltijd / 5 * VRprijs)
prijstot = personen * prijskaart + VRtotaaltijd / 5 * VRprijs

print("Dit geweldige dagje-uit met " + str(personen) + " mensen in de Speelhal met " + str(VRtijdpersoon) + " minuten VR kost je maar " + str(round(prijstot, 2)) + " euro.")