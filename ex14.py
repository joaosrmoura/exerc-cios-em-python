numero = input("Digite o numero da conta:")
saldo = float(input("Digite o saldo: R$"))
debito = float(input("Digite o débito da conta: R$"))
credito = float(input("Digite o crédito da conta: R$"))

saldoatual = saldo - debito + credito

if saldoatual >= 0:
    print(f"O saldo R${saldoatual} é positivo")
else:
    print(f"O saldo R${saldoatual} é negativo")
