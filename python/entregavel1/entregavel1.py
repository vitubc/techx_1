print("=== Calculadora de troco ===")
valor_compra = float(input("Digite o valor da compra: R$ "))
valor_pago = float(input("Digite o valor pago: R$ "))
troco = valor_pago - valor_compra
print(f"Troco: R$ {troco:.2f}")

print("\n=== Média de notas ===")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
media = (nota_1 + nota_2 + nota_3) / 3
print(f"Média: {media:.2f}")

print("\n=== Conversor de tempo ===")
total_segundos = int(input("Digite o valor em segundos: "))
horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60
print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")

print("\n=== Calculadora de desconto ===")
preco_produto = float(input("Digite o preço do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
valor_desconto = preco_produto * percentual_desconto / 100
preco_final = preco_produto - valor_desconto
print(f"Preço final: R$ {preco_final:.2f}")

print("\n=== Par ou ímpar ===")
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

print("\n=== Inversor de nome ===")
nome = input("Digite um nome: ")
nome_invertido = nome[::-1]
print(f"Nome invertido: {nome_invertido}")
