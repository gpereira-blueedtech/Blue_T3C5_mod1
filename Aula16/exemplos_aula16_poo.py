# class Mamifero():
#     # Criando o método construtor, ele vai servir para já passar todos
#     # os atributos para os objetos que eu for criando
#     def __init__(self, nome, pelo, cor, idade, tamanho = "pequeno"): 
#         self.nome = nome
#         self.pelo = pelo
#         self.cor = cor
#         self.tamanho = tamanho
#         self.idade = idade

#     def crescer(self, anos = 10):
#         self.idade += anos

#     def locomover(self):
#         print("Elx está andando")
    
#     def comer(self): 
#         self.tamanho = "grande"
    
#     def dados(self):
#         dados = f"Nome: {self.nome}\nPelo:{self.pelo}"
#         return dados
        
# cachorro = Mamifero("Eddie","curto","preto",1)

# print(type(cachorro))
# print(vars(cachorro))
# print(type(vars(cachorro)))

# print()
# cachorro.crescer()
# cachorro.locomover()
# cachorro.comer()
# print(vars(cachorro))

# print()
# print(cachorro.nome)
# print(cachorro.dados())


# 1.a) Crie uma classe pessoa com os seguintes atributos: nome, sobrenome e idade.
# 1.b) Acrescente a classe criada um método para mostrar os dados de uma pessoa.
# 1.c) Crie um objeto do tipo pessoa para testar suas propriedades e métodos.

class pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
    def getdados(self):
        print(self.nome, self.sobrenome, self.idade)
        return [self.nome,self.sobrenome,self.idade]
        

gustavo = pessoa("Gustavo","Batata",27)

guardar = gustavo.getdados()
print(guardar)