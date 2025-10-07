litros = float(input("Quantidade de litros vendidos: "))
tipo = input("Tipo de combustível (A - álcool, G - gasolina): ").upper()

if tipo == "A":
    preco_litro = 1.90
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
elif tipo == "G":
    preco_litro = 2.50
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
else:
    print("Tipo de combustível inválido!")
    exit()

preco_total = litros * preco_litro
valor_desconto = preco_total * desconto
valor_pagar = preco_total - valor_desconto

print(f"Valor a pagar: R$ {valor_pagar:.2f}")
