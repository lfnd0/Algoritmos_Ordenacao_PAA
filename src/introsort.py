def introsort(lista):
    profundidade_maxima = (len(lista).bit_length() - 1) * 2
    introsort_auxiliar(lista, 0, len(lista), profundidade_maxima)

def introsort_auxiliar(lista, inicio, fim, profundidade_maxima):
    if fim - inicio <= 1:
        return
    elif profundidade_maxima == 0:
        heapsort(lista, inicio, fim)
    else:
        p = particao(lista, inicio, fim)
        introsort_auxiliar(lista, inicio, p + 1, profundidade_maxima - 1)
        introsort_auxiliar(lista, p + 1, fim, profundidade_maxima - 1)

def particao(lista, inicio, fim):
    pivo = lista[inicio]
    i = inicio - 1
    j = fim

    while True:
        i = i + 1
        while lista[i] < pivo:
            i = i + 1
        j = j - 1
        while lista[j] > pivo:
            j = j - 1
        if i >= j:
            return j
        troca(lista, i, j)

def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def heapsort(lista, inicio, fim):
    construcao_heap_maximo(lista, inicio, fim)
    for i in range(fim - 1, inicio, -1):
        troca(lista, inicio, i)
        heap_maximo(lista, indice = 0, inicio = inicio, fim = i)

def construcao_heap_maximo(lista, inicio, fim):
    def parente(i):
        return (i - 1) // 2
        comprimento = fim - inicio
        indice = parente(comprimento - 1)
        while indice >= 0:
            heap_maximo(lista, indice, inicio, fim)
            indice = indice - 1

def heap_maximo(lista, indice, inicio, fim):
    def esquerda(i):
        return 2 * i + 1
    def direita(i):
        return 2 * i + 2
    
    tamanho = fim - inicio
    e = esquerda(indice)
    d = direita(indice)
    if(e < tamanho and lista[inicio + e] > lista[inicio + indice]):
        maior = e
    else:
        maior = indice
    if(d < tamanho and lista[inicio + d] > lista[inicio + maior]):
        maior = d
    if maior != indice:
        troca(lista, inicio + maior, inicio + indice)
        heap_maximo(lista, maior, inicio, fim)