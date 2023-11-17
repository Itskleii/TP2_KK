nb = int(input("entrez un nombre: "))


if (nb > 0) and (nb%2==0):
    print("positif et pair")

if (nb > 0) and (nb%2!=0):
    print("positif et impair")


if nb == 0:
    print("est égale à 0 et est pair")


if nb < 0 and nb%2==0:
    print("negatif et pair")

if nb < 0 and nb%2 !=0:
    print("negatif et impair")

