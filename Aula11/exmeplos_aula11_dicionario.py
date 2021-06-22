# contatos_lista = [('Gustavo', '1234-5678'), ('Pedro', '9999-9999'),
# ('Ana', '8765-4321'), ('Marina', '7788-8877')]

# dicionario1 = {"Chave":[30,"valor"]} 
# print(type(dicionario1))
# print(dicionario1)

# print(contatos_lista)
# print(type(contatos_lista))

# contatos = dict(contatos_lista) # Transforma a lista em dicionario e armazena em contatos

# print(contatos)
# print(type(contatos))
# print(contatos['Gustavo'])
# print()

# dic1 = {'Gustavo':['Silva','1234-5678'], 'Ana':'555-666','Janice':'8765-4321','Marina':'7788-8877'}
# nome = input("Digite o nome da pessoa: ").title()

# print(dic1.get(nome)) # Retorna o valor da chave passada, e caso não seja encontrada, retorna a mensagem de erro escolhida
# # print(dic1['Gustavo Silva']) # Retorna o valor da chave passada, mas pual exceção caso não seja encontrada

# vingadores = {"Chris Evans":"Capitão América", "Mark Ruffalo":"Hulk","Tom Hiddleston":"Loki",
# "Chris Hemsworth":"Thor","Robert Downey Jr":"Homem de Ferro","Scarlett Johansson":"Viúva Negra"}

# print("Chris Evans" in vingadores.keys()) # Verifica se um elemento está presente nas chaves do dicionário
# print("Hulk" in vingadores.values()) # Verifica se um elemento está presente nos valores do dicionário

# vingadores ["Robert Deniro"] = "Batman" # Adicionando uma nova chave e valor ao dicionário

# nome = input("Digite o nome do ator: ")
# personagem = input("Digite o nome do personagem: ")
# print()
# vingadores[nome] = personagem # Adicionando nova chave e valor através de input
# print(vingadores)
# print()
# del vingadores["Robert Deniro"]
# print(vingadores)








# ### EXERCÍCIO 1:
# # 2 – Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 
# # (que podem ser armazenados em uma lista) e seus valores correspondentes aos 
# # quadrados desses números.

# # dicionario[chave] = valor # sintaxe para adicionar um elemento novo ao dicionario

# numeros_quadrados = dict()
# lista_numero = [1, 4, 5, 6, 7, 9]

# for n in lista_numero:
#     numeros_quadrados[n] = n**2

### B – Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10]
### e cada valor associado é o número ao quadrado.​

# quadrados2 = {}

# for n in range(1,11): # range: cria uma sequência de números até o valor dado -1
#     quadrados2[n] = n**2

# quadrados3 = {}
# numero = int(input("Digite um valor inteiro: "))
# for n in range(1,numero+1): # range: cria uma sequência de números até o valor dado -1
#     quadrados3[n] = n**2

# print(numeros_quadrados)
# print()
# print(quadrados2)
# print()
# print(quadrados3)







vingadores = {"Chris Evans":"Capitão América", "Mark Ruffalo":"Hulk","Tom Hiddleston":"Loki",
"Chris Hemsworth":"Thor","Robert Downey Jr":"Homem de Ferro","Scarlett Johansson":"Viúva Negra"}
print(vingadores)
print()


while True:
    ator = input("Digite o nome do ator para remover da lista, ou 0 para sair: ")
    if ator == "0":
        break
    print(vingadores.pop(ator,"Ator não encontrado nessa lista."))

print(vingadores)

# deletados = vingadores.pop(ator,"Ator não encontrado nessa lista.")
# print(vingadores.pop(ator,"Ator não encontrado nessa lista."))
# print(vingadores)
# print()
# print("O personagem deletado foi:",deletados)






### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

produtos = {"batata":10, "Chocolate":0}