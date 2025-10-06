nome = input("Digite o nome:")
idade = int(input("Digite a idade:"))

if idade >= 0 and idade <= 2:
    tipo = "bebe"
elif idade >= 3 and idade <= 11:
    tipo = "criança"
elif idade >= 12 and idade <= 21:
    tipo = "jovem"
elif idade >= 22 and idade <= 64:
    tipo = "adulto"
elif idade >= 65 and idade <= 100:
    tipo = "idoso"
elif idade >= 101:
    tipo = "muito velhinho"
else:
    tipo = "idade invalida"
   
print(f"{nome} tem {idade} anos, e o tipo de acordo com a tabela é: {tipo}")