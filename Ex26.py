preco_aquisicao = float(input("Digite o preço de aquisição do produto: "))

if preco_aquisicao < 50:
    preco_venda = preco_aquisicao * 1.45
else:
    preco_venda = preco_aquisicao * 1.30

print(f"Preço de venda: R$ {preco_venda:.2f}")
