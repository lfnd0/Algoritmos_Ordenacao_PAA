import random
from introsort import introsort

lista = random.sample(range(101), 100)
lista = [int(x) for x in lista]
introsort(lista)

print('Resultado: ', end='')
print(lista)