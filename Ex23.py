qtd_frangos = int(input("Quantidade de frangos: "))
custo_chip = 4.00
custo_anel = 3.50

total = qtd_frangos * (custo_chip + 2 * custo_anel)
print(f"Gasto total da granja: R$ {total:.2f}")
