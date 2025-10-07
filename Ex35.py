tipo = input("Tipo de carne (File Duplo, Alcatra, Picanha): ").strip().lower()
quantidade = float(input("Quantidade (kg): "))
pagamento = input("Pagamento com cartão Tabajara? (S/N): ").upper()

if tipo == "file duplo":
    preco = 34.90 if quantidade <= 5 else 35.80
elif tipo == "alcatra":
    preco = 44.90 if quantidade <= 5 else 46.80
elif tipo == "picanha":
    preco = 66.90 if quantidade <= 5 else 67.80
else:
    print("Tipo de carne inválido!")
    exit()

total = preco * quantidade
desconto = total * 0.05 if pagamento == "S" else 0
total_pagar = total - desconto

print("\nCUPOM FISCAL")
print(f"Tipo de carne: {tipo.title()}")
print(f"Quantidade: {quantidade} kg")
print(f"Preço total: R$ {total:.2f}")
print(f"Tipo de pagamento: {'Cartão Tabajara' if pagamento == 'S' else 'Outro'}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_pagar:.2f}")
