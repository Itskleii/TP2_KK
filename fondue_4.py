BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400


nbConvives = int(input("Combien de convive attendez vous?"))


qte_frg = (fromage * nbConvives / BASE)
qte_eau = (eau * nbConvives / BASE)
qte_ail = (ail * nbConvives / BASE)
qte_pain = (pain * nbConvives / BASE)









print("Pour faire une fondue fribourgeoise pour" ,nbConvives, "personnes, il vous faut:")
print(qte_frg, "gr de fromage")
print(qte_eau,"l d'eau")
print(qte_ail, "gousses d'ail")
print(qte_pain,"gr de pain")

