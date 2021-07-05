
class Remedio:
    def __init__(self, posologia, principio_ativo, laboratorio, preco, faixa_etaria, 
    efeito_colateral, tarja, nome):
        self.posologia = posologia+" ao dia"
        self.principio_ativo = principio_ativo
        self.__laboratorio = laboratorio
        self.preco = preco
        self.faixa_etaria = faixa_etaria
        self.efeito_colateral = efeito_colateral 
        self.tarja = tarja
        self.nome = nome

    def printa_remedio(self,sintoma):
        if sintoma == "dor de cabeça":
            return f"Você deve tomar {self.nome}"
        else:
            return "Vish, não sei te ajudar.. =("

    def getPosologia(self):
        return self.posologia
    
    def setPosologia(self, nova_poso):
        self.posologia = nova_poso
        
    def getPreco(self):
        return self.preco

    @property
    def laboratorio(self):
        return self.__laboratorio

    @laboratorio.setter
    def laboratorio(self, novo_lab):
        raise ValueError("Use o método setLaboratorio")

    def setLaboratorio(self, novo_lab):
        self.__laboratorio = novo_lab

    



if __name__ == "__main__":
    buscopan = Remedio("3 vezes","escopolamina","Boehringer",17,12,
    ["Reações na pele", "urticária (placas elevadas na pele, geralmente com coceira)","coceiras", "taquicardia", "boca seca", "alteração na produção de suor"],
    "livre","Buscopan")

    # print(buscopan.posologia) # me retorna o atributo
    # print(buscopan.efeito_colateral) #retorna a lista, e eu consigo trabalhar normalmente como qualquer outra lista
    # print()
    # print(type(buscopan.posologia))
    # print(type(buscopan.efeito_colateral))
    # print()
    # print(buscopan.efeito_colateral[0])
    # print()
    # buscopan.efeito_colateral.pop(0)
    # print(buscopan.efeito_colateral)
    print()
    
    # print(buscopan.getPosologia())
    # print()
    # nova = input("Qual a nova posologia?")
    # buscopan.setPosologia(nova) 
    # print(buscopan.getPosologia())
    # print()
    # compra = buscopan.getPreco() * 3
    # print(compra)

    print(buscopan.laboratorio)
    # buscopan.laboratorio = "Novo"
    buscopan.nome = "Buscopan composto"
    buscopan.laboratorio = "novo lab"

    buscopan.setLaboratorio("novo")
    print(buscopan.laboratorio)
    print(buscopan.nome)
