"""Funções para realizar operações matemáticas básicas."""


def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b


# Versão em Portugol:
# funcao real somar(real a, real b)
#     retorne a + b
# fimfuncao


def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b


# Versão em Portugol:
# funcao real subtrair(real a, real b)
#     retorne a - b
# fimfuncao


def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b


# Versão em Portugol:
# funcao real multiplicar(real a, real b)
#     retorne a * b
# fimfuncao


def dividir(a, b):
    """Retorna a divisão de dois números ou None quando o divisor é zero."""
    if b == 0:
        return None

    return a / b


# Versão em Portugol:
# funcao real dividir(real a, real b)
#     se (b == 0) entao
#         escreva("Não é possível dividir por zero")
#         retorne 0
#     fimse
#     retorne a / b
# fimfuncao
