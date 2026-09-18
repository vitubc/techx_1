"""Script principal para demonstrar o uso dos módulos da Semana 03."""

import estatistica as est

from calculadora import dividir, multiplicar, somar, subtrair
from utilidades import (
    adicionar_item,
    calcular_caixa,
    converter_temperatura,
    criar_ficha_aluno,
    fatorial,
    relatorio,
    validar_senha,
)


print("=== Calculadora ===")
print(f"Soma: {somar(10, 5)}")
print(f"Subtração: {subtrair(10, 5)}")
print(f"Multiplicação: {multiplicar(10, 5)}")
print(f"Divisão: {dividir(10, 5)}")

resultado_divisao = dividir(10, 0)

if resultado_divisao is None:
    print("Divisão por zero não permitida.")

print("\n=== Utilidades ===")
print(f"25 °C equivalem a {converter_temperatura(25):.1f} °F")
print(f"A senha é válida? {validar_senha('python123')}")
print(f"Total da compra: R$ {calcular_caixa(10.50, 20, 5.25):.2f}")

ficha = criar_ficha_aluno(nome="Ana", idade=18, curso="Python")
print(f"Ficha do aluno:\n{ficha}")

lista_original = ["caderno", "lápis"]
lista_nova = adicionar_item(lista_original, "borracha")
print(f"Lista original: {lista_original}")
print(f"Nova lista: {lista_nova}")

print("\n=== Desafios bônus ===")
numeros = [2, 3, 3, 5, 7]
print(f"Média: {est.media(numeros):.2f}")
print(f"Mediana: {est.mediana(numeros)}")
print(f"Moda: {est.moda(numeros)}")
print(f"Fatorial de 5: {fatorial(5)}")

texto_relatorio = relatorio(
    "Resumo do aluno",
    "Atividade concluída",
    "Módulos testados",
    autor="Ana",
    turma="Semana 03",
)
print(texto_relatorio)

# Versão simplificada em Portugol do script principal:
# importe calculadora, utilidades, estatistica
# escreva(calculadora.somar(10, 5))
# escreva(utilidades.converter_temperatura(25))
# escreva(utilidades.validar_senha("python123"))
# escreva(estatistica.media([2, 3, 3, 5, 7]))
