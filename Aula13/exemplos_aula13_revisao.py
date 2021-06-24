# lista = ["Eduardo","Luis","Janice","Carlos","Mariana"]

# lista[2] = "Guilherme" # Altera o valor do índice 2 da lista
# print()
# print(lista[4])

# for item in lista: # interage com os elementos da lista, não com os índice
#     print(item)
#     lista[item] = input("Digite o novo valor") #quebra, porque o que está em "item" não é um índice


# for indice, elemento in enumerate(lista,50):
#     print(indice)
#     print(elemento)
#     print(type(elemento))
#     lista[indice] = input(f"Digite o valor para substituir {elemento} no índice {indice}: ")

# for item in range(lista): #range(5) #0, 1, 2, 3, 4
#     print(item)
#     lista[item] = input(f"Digite o novo valor para o índice {item}")

# lista_composta = ["Eduardo","Luis","Janice",["Carlos",["Mariana","Steffany"]]]
# print(lista_composta[3][1][1])

# tupla = ("Eduardo","Luis","Janice",("Carlos",("Mariana","Steffany")))
# print(tupla[3][1][1])
# tupla[1] = "Wanderson"


dicionario1 = {"Aluno":"Max","Idade":"20","Média":7}
# print(len(dicionario1))
# print(dicionario1.keys())
# print(dicionario1.values())
# print()

# print(dicionario1["Aluno"])
# print()

# for i in dicionario1:
#     print(i)
#     dicionario1[i] = input("Digite o novo valor: ")
#     print(dicionario1)
# print()

# for i in dicionario1.items():
#     print(i)
# print()

# for k,v in dicionario1.items():
#     print(k,v)
#     print(f"A chave {k} tem o valor {v}")
# print()

# for i in dicionario1.keys():
#     print(i)
# print()

# for i in dicionario1.values():
#     print(i)
# print()

# print(dicionario1)

dicionario2 = {"Aluno":"Gabriel","Idade":"15","Situação":"Aprovado"}
# dicionario1.update(dicionario2) # Insere um dicionário dentro de outro substituindo os valores das chaves que forem iguais
# print(dicionario1)

lista_dic = [dicionario1, dicionario2]
print(lista_dic[0]["Aluno"])
print()
for i in lista_dic:
    print(i)
    print(i["Aluno"])
