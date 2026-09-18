print("=== Classificador de Cliente ===")
idade = int(input("Digite a idade do cliente: "))
renda = float(input("Digite a renda mensal do cliente: R$ "))

if idade < 18 or renda < 2000:
    categoria = "Bronze"
elif renda < 5000:
    categoria = "Prata"
elif renda < 10000:
    categoria = "Ouro"
else:
    categoria = "Diamante"

print(f"Categoria do cliente: {categoria}")

# Versão Portugol:
# escreva("Digite a idade e a renda: ")
# leia(idade, renda)
# se (idade < 18 ou renda < 2000) entao
#     categoria = "Bronze"
# senao se (renda < 5000) entao
#     categoria = "Prata"
# senao se (renda < 10000) entao
#     categoria = "Ouro"
# senao
#     categoria = "Diamante"
# fimse
# escreva("Categoria: ", categoria)

print("\n=== Menu de Operações Matemáticas ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Escolha uma operação: "))
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

match opcao:
    case 1:
        resultado = primeiro_numero + segundo_numero
        print(f"Resultado da soma: {resultado}")
    case 2:
        resultado = primeiro_numero - segundo_numero
        print(f"Resultado da subtração: {resultado}")
    case 3:
        resultado = primeiro_numero * segundo_numero
        print(f"Resultado da multiplicação: {resultado}")
    case 4:
        if segundo_numero != 0:
            resultado = primeiro_numero / segundo_numero
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Não é possível dividir por zero.")
    case _:
        print("Opção inválida.")

# Versão Portugol:
# escreva("1-Soma  2-Subtração  3-Multiplicação  4-Divisão")
# leia(opcao, primeiro_numero, segundo_numero)
# escolha opcao
#     caso 1: resultado = primeiro_numero + segundo_numero
#     caso 2: resultado = primeiro_numero - segundo_numero
#     caso 3: resultado = primeiro_numero * segundo_numero
#     caso 4: resultado = primeiro_numero / segundo_numero
#     outrocaso: escreva("Opção inválida")
# fimescolha
# escreva("Resultado: ", resultado)

print("\n=== Análise de Números ===")
soma = 0
maior_numero = None
menor_numero = None

for contador in range(1, 6):
    numero = float(input(f"Digite o {contador}º número: "))
    soma += numero

    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

    if menor_numero is None or numero < menor_numero:
        menor_numero = numero

media = soma / 5

print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior valor: {maior_numero}")
print(f"Menor valor: {menor_numero}")

# Versão Portugol:
# soma = 0
# para contador de 1 ate 5 faca
#     escreva("Digite um número: ")
#     leia(numero)
#     soma = soma + numero
#     se (contador == 1) entao
#         maior_numero = numero
#         menor_numero = numero
#     senao
#         se (numero > maior_numero) entao maior_numero = numero fimse
#         se (numero < menor_numero) entao menor_numero = numero fimse
#     fimse
# fimpara
# media = soma / 5
# escreva("Soma: ", soma, " Média: ", media)
# escreva(" Maior: ", maior_numero, " Menor: ", menor_numero)

print("\n=== Sistema de Autenticação ===")
senha_correta = "python123"
tentativas = 0
acesso_liberado = False

while tentativas < 3 and not acesso_liberado:
    senha_digitada = input("Digite a senha: ")

    if senha_digitada == senha_correta:
        acesso_liberado = True
        print(f"Acesso liberado após {tentativas + 1} tentativa(s).")
    else:
        tentativas += 1
        print(f"Senha incorreta. Tentativas restantes: {3 - tentativas}")

if not acesso_liberado:
    print("Acesso bloqueado após 3 tentativas incorretas.")

# Versão Portugol:
# senha_correta = "python123"
# tentativas = 0
# enquanto (tentativas < 3) faca
#     escreva("Digite a senha: ")
#     leia(senha_digitada)
#     se (senha_digitada == senha_correta) entao
#         escreva("Acesso liberado")
#         pare
#     senao
#         tentativas = tentativas + 1
#     fimse
# fimenquanto
# se (tentativas == 3) entao
#     escreva("Acesso bloqueado")
# fimse
