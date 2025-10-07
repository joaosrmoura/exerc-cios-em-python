peso = float(input("Peso dos peixes (kg): "))

excesso = max(0, peso - 50)
multa = excesso * 4

print(f"Excesso: {excesso} kg")
print(f"Multa a pagar: R$ {multa:.2f}")
