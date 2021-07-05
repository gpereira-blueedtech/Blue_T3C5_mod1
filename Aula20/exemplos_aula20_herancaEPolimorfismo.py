class Pessoa:
    def __init__(self, olhos, altura, peso, idade):
        self.olhos = olhos
        self.altura = altura
        self.peso = peso
        self.idade = idade

    def envelhecer(self,anos = 1):
        self.idade += anos

    def trabalhar(self):
        print("Você não tem emprego.")

class Medico(Pessoa):
    def __init__(self,olhos,altura,peso,idade,crm):
        super().__init__(olhos, altura, peso, idade)
        self.crm = crm 

    def medicar(self):
        print("Você foi medicado. Que bom.")

    def trabalhar(self):
        print("Você vai trabalhar no consultório")
    

class Neuro(Medico):
    def __init__(self,olhos,altura,peso,idade, crm, especialidade):
        super().__init__(olhos,altura,peso,idade,crm)
        self.especialidade = especialidade 

class Advogado(Pessoa):
    def __init__(self,olhos,altura,peso,idade,oab):
        super().__init__(olhos, altura, peso, idade)
        self.oab = oab 

    def trabalhar(self):
        print("Você vai trabalhar no escritório")

pessoa = Pessoa("castanho", 1.80, 80, 20)

medico = Medico("castanho", 1.80, 80, 20,"123456")
advogado = Advogado("Azul",1.6,80,30,"456789")

neuro = Neuro("castanho", 1.80, 80, 20,"123456","Cabeça")

# print(pessoa.idade)
# pessoa.envelhecer()
# print(pessoa.idade)
# print()
# print(medico.idade)
# medico.envelhecer(5)
# print(medico.idade)
# print()
# medico.medicar()
# medico.crm = "123456"
# print(medico.crm)

# print(vars(medico))
# print()
# print(vars(neuro))
print(medico.idade)
print(advogado.idade)
pessoa.trabalhar()
medico.trabalhar()
advogado.trabalhar()
medico.envelhecer(5)
advogado.envelhecer(2)
print()
print(medico.idade)
print(advogado.idade)