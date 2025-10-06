pequenas = int(input("Quantidade de camisetas pequenas: "))
medias = int(input("Quantidade de camisetas médias: "))
grandes = int(input("Quantidade de camisetas grandes: "))

total = (pequenas * 10) + (medias * 12) + (grandes * 15)
print(f"Valor total da compra: R$ {total:.2f}")
