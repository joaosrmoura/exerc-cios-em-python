valor = int(input("Digite o valor do saque (10 a 600): "))

if 10 <= valor <= 600:
    notas100 = valor // 100
    valor %= 100
    notas50 = valor // 50
    valor %= 50
    notas10 = valor // 10
    valor %= 10
    notas5 = valor // 5
    notas1 = valor % 5

    print(f"Notas de 100: {notas100}")
    print(f"Notas de 50: {notas50}")
    print(f"Notas de 10: {notas10}")
    print(f"Notas de 5: {notas5}")
    print(f"Notas de 1: {notas1}")
else:
    print("Valor inválido para saque.")
