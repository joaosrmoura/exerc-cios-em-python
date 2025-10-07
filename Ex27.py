feminino_altas = 0
masculinos_bons = 0
total_masculinos = 0

for i in range(1, 51):
    print(f"\nAluno {i}:")
    matricula = input("Matrícula: ")
    sexo = input("Sexo (M/F): ").upper()
    altura = float(input("Altura (cm): "))
    status = int(input("Status físico (1-bom, 2-regular, 3-ruim): "))

    if sexo == "F" and altura > 170:
        feminino_altas += 1
    if sexo == "M":
        total_masculinos += 1
        if status == 1:
            masculinos_bons += 1

if total_masculinos > 0:
    percentual_bons = (masculinos_bons / total_masculinos) * 100
else:
    percentual_bons = 0

print(f"\nQuantidade de alunas com mais de 170cm: {feminino_altas}")
print(f"Percentual de alunos masculinos com status bom: {percentual_bons:.2f}%")
