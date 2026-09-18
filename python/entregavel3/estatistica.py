"""Funções simples para cálculos estatísticos."""


def media(numeros):
    """Retorna a média dos números recebidos."""
    return sum(numeros) / len(numeros)


# Versão simplificada em Portugol:
# funcao real media(lista numeros)
#     retorne soma(numeros) / tamanho(numeros)
# fimfuncao


def mediana(numeros):
    """Retorna a mediana dos números recebidos."""
    numeros_ordenados = sorted(numeros)
    quantidade = len(numeros_ordenados)
    meio = quantidade // 2

    if quantidade % 2 == 0:
        return (numeros_ordenados[meio - 1] + numeros_ordenados[meio]) / 2

    return numeros_ordenados[meio]


# Versão simplificada em Portugol:
# funcao real mediana(lista numeros)
#     ordene(numeros)
#     meio = tamanho(numeros) / 2
#     se (tamanho(numeros) % 2 == 0) entao
#         retorne (numeros[meio - 1] + numeros[meio]) / 2
#     fimse
#     retorne numeros[meio]
# fimfuncao


def moda(numeros):
    """Retorna o número que aparece mais vezes na lista."""
    numero_modal = numeros[0]
    maior_frequencia = 0

    for numero in numeros:
        frequencia = numeros.count(numero)

        if frequencia > maior_frequencia:
            maior_frequencia = frequencia
            numero_modal = numero

    return numero_modal


# Versão simplificada em Portugol:
# funcao real moda(lista numeros)
#     para cada numero em numeros faca
#         conte quantas vezes o numero aparece
#         guarde o numero com a maior frequência
#     fimpara
#     retorne numero_modal
# fimfuncao
