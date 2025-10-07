altura = float(input("Digite a altura (em metros): "))
sexo = input("Digite o sexo (M/F): ").upper()

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = None
    print("Sexo inválido!")

if peso_ideal is not None:
    print(f"Peso ideal: {peso_ideal:.2f} kg")
