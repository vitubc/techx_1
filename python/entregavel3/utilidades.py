"""Funções úteis para os exercícios da Semana 03."""


def converter_temperatura(celsius):
    """Converte uma temperatura de Celsius para Fahrenheit."""
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


# Versão simplificada em Portugol:
# funcao real converter_temperatura(real celsius)
#     retorne celsius * 9 / 5 + 32
# fimfuncao


def validar_senha(senha):
    """Retorna True quando a senha possui pelo menos oito caracteres."""
    return len(senha) >= 8


# Versão simplificada em Portugol:
# funcao logico validar_senha(cadeia senha)
#     retorne comprimento(senha) >= 8
# fimfuncao


def calcular_caixa(*precos):
    """Recebe vários preços e retorna o valor total da compra."""
    total = 0

    for preco in precos:
        total += preco

    return total


# Versão simplificada em Portugol:
# funcao real calcular_caixa(lista precos)
#     total = 0
#     para cada preco em precos faca
#         total = total + preco
#     fimpara
#     retorne total
# fimfuncao


def criar_ficha_aluno(**dados):
    """Recebe dados nomeados e retorna a ficha do aluno em texto."""
    ficha = ""

    for campo, valor in dados.items():
        ficha += f"{campo}: {valor}\n"

    return ficha.strip()


# Versão simplificada em Portugol:
# funcao cadeia criar_ficha_aluno(dicionario dados)
#     ficha = ""
#     para cada campo, valor em dados faca
#         ficha = ficha + campo + ": " + valor
#     fimpara
#     retorne ficha
# fimfuncao


def adicionar_item(lista_original, item):
    """Adiciona um item a uma cópia sem alterar a lista original."""
    nova_lista = lista_original.copy()
    nova_lista.append(item)
    return nova_lista


# Versão simplificada em Portugol:
# funcao lista adicionar_item(lista lista_original, cadeia item)
#     nova_lista = copiar(lista_original)
#     adicione item em nova_lista
#     retorne nova_lista
# fimfuncao


def fatorial(numero):
    """Calcula o fatorial de um número inteiro usando recursão."""
    if numero <= 1:
        return 1

    return numero * fatorial(numero - 1)


# Versão simplificada em Portugol:
# funcao inteiro fatorial(inteiro numero)
#     se (numero <= 1) entao
#         retorne 1
#     fimse
#     retorne numero * fatorial(numero - 1)
# fimfuncao


def relatorio(titulo, *linhas, **config):
    """Monta um relatório com título, linhas e configurações adicionais."""
    texto = f"=== {titulo} ===\n"

    for linha in linhas:
        texto += f"{linha}\n"

    for chave, valor in config.items():
        texto += f"{chave}: {valor}\n"

    return texto.strip()


# Versão simplificada em Portugol:
# funcao cadeia relatorio(cadeia titulo, lista linhas, dicionario config)
#     texto = titulo
#     para cada linha em linhas faca
#         texto = texto + linha
#     fimpara
#     para cada chave, valor em config faca
#         texto = texto + chave + ": " + valor
#     fimpara
#     retorne texto
# fimfuncao
