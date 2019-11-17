import random
from algoritmo import introsort

def criar_lista(tamanho, ordenacao):
    numeros = [random.randrange(tamanho) for x in range(tamanho)]
    if ordenacao == 'D':
        return sorted(numeros, reverse=True)
    elif ordenacao == 'C':
        return sorted(numeros)
    elif ordenacao == 'N':
        return numeros

tamanho = 1000
ordenacao = "D"

lista = criar_lista(tamanho, ordenacao)
print("Lista gerada: ")
print(lista)

lista = [int(x) for x in lista]
introsort(lista)
print("Lista ordenada: ")
print(lista)