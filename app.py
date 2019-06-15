#Calcolo del Pi greco attraverso il metodo montecarlo

import random

num_tentativi = 999999
num_cerchio = 0

for lanci in range(num_tentativi):
    x = random.random()
    y = random.random()
    #Determino se il punto è appartenente al cerchio
    if (x ** 2 + y ** 2 <= 1):
        num_cerchio += 1

pigreco = 4 * num_cerchio / num_tentativi
print("tentativi=%d, numeri appartenti al cerchio=%d, Pi=%.4f" % (num_tentativi, num_cerchio, pigreco))