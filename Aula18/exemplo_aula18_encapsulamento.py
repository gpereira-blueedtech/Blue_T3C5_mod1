class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhadas = 0
        self.__salario = 0

    @property
    def salario(self):
        print("Essa informação é sigilosa")
        return self.__salario

    @salario.setter
    def salario(self, novo_valor):
        raise ValueError("Use o método apropriado, calcula_salario")
        

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada

eduardo = Funcionario("Eduardo","Dev Senior",100)

# eduardo.registra_hora_trabalhada()
# eduardo.registra_hora_trabalhada()
# eduardo.registra_hora_trabalhada()
# eduardo.registra_hora_trabalhada()
# eduardo.registra_hora_trabalhada()
# eduardo.calcula_salario()

print(eduardo.nome)
print(eduardo.salario)

eduardo.nome = "José"
eduardo.salario = 500