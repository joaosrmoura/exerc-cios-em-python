qtd_sanduiches = int(input("Quantidade de sanduíches: "))

queijo = (2 * 50 * qtd_sanduiches) / 1000  # em kg
presunto = (50 * qtd_sanduiches) / 1000
carne = (100 * qtd_sanduiches) / 1000

print(f"Queijo: {queijo:.2f} kg")
print(f"Presunto: {presunto:.2f} kg")
print(f"Carne: {carne:.2f} kg")
