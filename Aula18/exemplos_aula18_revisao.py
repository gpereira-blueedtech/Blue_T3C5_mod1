class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo   

    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo

    def depositar(self):
        valor = float(input("Digite o valor a depositar: "))
        self.saldo += valor

    def mostraSaldo(self):
        return self.saldo


cliente1 = Conta("Gustavo",50000)
cliente2 = Conta("Gabriel",500)
cliente3 = Conta("Marcos",10)
cliente4 = Conta("Janice",500000)


# print(cliente1.titular, cliente1.saldo)
# print(cliente2.titular, cliente2.saldo)
# print(cliente3.titular, cliente3.saldo)
# print(cliente4.titular, cliente4.saldo)

# valor_saque = float(input("Digite o valor a sacar: "))
# saldo_cliente = cliente1.sacar(valor_saque)
# print(saldo_cliente)

# print(cliente1.titular, cliente1.saldo)
# print(cliente2.titular, cliente2.saldo)
# print(cliente3.titular, cliente3.saldo)
# print(cliente4.titular, cliente4.saldo)

# cliente3.saldo = 99999999

# print(cliente3.saldo)

