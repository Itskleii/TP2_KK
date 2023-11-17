import random

nb = random.randint(1,3)
print("le nombre est : ", nb)

if nb < 3:
    print('pile')
else:
    print('face')