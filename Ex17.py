salario = float(input("Digite o salário atual: "))

if salario <= 280:
    aumento = 0.20
elif salario <= 700:
    aumento = 0.15
elif salario <= 1500:
    aumento = 0.10
else:
    aumento = 0.05

valor_aumento = salario * aumento
novo_salario = salario + valor_aumento

print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento: {aumento * 100}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
