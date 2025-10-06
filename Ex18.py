valor_hora = float(input("Valor da hora: "))
horas_trabalhadas = float(input("Horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

# IR
if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
else:
    ir = salario_bruto * 0.20

inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11
total_descontos = ir + inss
salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"(-) IR: R$ {ir:.2f}")
print(f"(-) INSS: R$ {inss:.2f}")
print(f"FGTS: R$ {fgts:.2f}")
print(f"Total de Descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
