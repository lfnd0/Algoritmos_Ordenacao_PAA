import random
from quicksort import quicksort

def criar_lista(tamanho, ordenacao):
    numeros = [random.randrange(tamanho) for x in range(tamanho)]
    if ordenacao == 'D':
        return sorted(numeros, reverse=True)
    elif ordenacao == 'C':
        return sorted(numeros)
    elif ordenacao == 'A':
        return numeros

tamanho = 1000
ordenacao = "D"

lista = criar_lista(tamanho, ordenacao)
print("Lista gerada: ")
print(lista)

lista = [int(x) for x in lista]
quicksort(lista, 0, len(lista) - 1)
print("Lista ordenada: ")
print(lista)