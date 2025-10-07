num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Operações disponíveis: +, -, *, /")
operacao = input("Escolha a operação: ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2 if num2 != 0 else "Erro (divisão por zero)"
else:
    resultado = "Operação inválida"

print(f"Resultado: {resultado}")

if isinstance(resultado, (int, float)):
    if resultado % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

    if resultado > 0:
        print("Positivo")
    elif resultado < 0:
        print("Negativo")
    else:
        print("Zero")

    if resultado == int(resultado):
        print("Inteiro")
    else:
        print("Decimal")
