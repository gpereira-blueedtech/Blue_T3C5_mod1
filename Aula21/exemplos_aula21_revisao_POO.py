class bombaCombustivel: #  Criei a classe, as instruções para os objetos que serão criados
    def __init__(self, tipoCombustivel, valorCombustivel, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel # Sempre que estou me referindo à um atributo dentro do construtor, uso self.atributo
        self.valorCombustivel = valorCombustivel
        self.quantidadeCombustivel = quantidadeCombustivel

    def alterarValor(self, novo_valor): # Método, uma função dentro da classe
        self.valorCombustivel = novo_valor #alterando o valor de um atributo para o novo passado
        
    def alterarCombustivel(self, tipo_combustivel):
        self.tipoCombustivel = tipo_combustivel

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade
    
    
    def abastecerPorValor(self, valorAbastecido):
        litros_abastecidos = valorAbastecido / self.valorCombustivel
        print(f"Você abasteceu {litros_abastecidos} litros.")
        # self.quantidadeCombustivel = self.quantidadeCombustivel - litros_abastecidos # Maneira alternativa de fazer
        self.quantidadeCombustivel -= litros_abastecidos
        


bomba1 = bombaCombustivel("Gasolina Comum",5,1000) # Criando o objeto bomba1 com os 3 parâmetros pedidos no construtor da classe bombaCombustivel
# print("Valor bomba 1:")
# print(bomba1.valorCombustivel)
# print()

# bomba2 = bombaCombustivel("Etanol",4,2000)
# print("Valor bomba 2:")
# print(bomba2.valorCombustivel)
# print()

# bomba1.alterarValor(10)
# print("Valor bomba 1 depois de chamar o método:")
# print(bomba1.valorCombustivel)

print(bomba1.quantidadeCombustivel)
print()
valor = float(input("Quanto vai abastecer?\n"))
bomba1.abastecerPorValor(valor) #Chamando o método abastecerPorValor do objeto bomba1
print(bomba1.quantidadeCombustivel)