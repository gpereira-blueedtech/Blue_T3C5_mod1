# l = [10,20,30,40,50]
# # l = "Hoje está um pouco menos frio" # funciona do mesmo modo que strings

# print(l)
# print(type(l))
# print(l[0]) # retorna o valor no índice informado
# print(l[:3]) # retorna os valores até o indíce informado -1
# print(l[3:]) # retorna os valores a partir do índice informado
# print(l[1:3]) # retorna os valores entre o índice informado primeiro e o "último -1"


# l2 = [10,20,30,[40,50],60,"Rudhy",True,["Glauco", "Janice",[70,"Blue"]]]
# print(l2)
# print(type(l2))
# print(len(l2)) # retorna o tamanho da lista (o último índice é sempre o "tamanho -1")
# print(l2[7]) # retorna o valor no índice informado
# print(l2[:4]) # retorna os valores até o indíce informado -1
# print(l2[4:]) # retorna os valores a partir do índice informado
# print(l2[1:4]) # retorna os valores entre o índice informado primeiro e o "último -1"
# print(l2[3])
# print(l2[3][0]) # retorna o índice 0 do índice 3


# l = [10,20,30,40,50]
# print(l)
# print(len(l))
# print()

# l[3] = "Rafael" # Altero o valor do índice especificado
# l[3] = input("Digite o novo valor do índice")
# print(l)
### Quando Python utiliza o for, ele interage com o elemento e não com o índice, temos que utilizar range() para que for possa interagis com o índice.

### Não vai funcionar dessa maneira porque o Python não interage com o número do índice
### e sim com o valor dele (então na primeira iteração ele vai receber 10, e não 0)
# for indice_atual in l: 
#     print(indice_atual)
#     l[indice_atual] = input(f"Digite o novo valor para {indice_atual}: ")
#     print(l)

# for i in range(5):
#     print(i)

# print()
# for indice_atual in range(5): 
#     print(indice_atual)
#     l[indice_atual] = input(f"Digite o novo valor para {indice_atual}: ")
#     print(l) 

## range(5) vai criar (0,1,2,3,4)
## uso o range(len(lista)) para me retornar uma range com o tamanho da lista
## Dessa maneira consigo usar os índices da lista
# for indice_atual in range(len(l)):
#     print(indice_atual)
#     l[indice_atual] = input(f"Digite o valor para {indice_atual}: ")

l = [20,10,30,50,40]
s = ["5000","Blue", "C","A", "20","Dado", "10", "Dedo","Dabura"]
# print(min(l)) # retorna o valor mínimo da lista
# print(max(l))# retorna o valor máximo da lista
# print()
# print(min(s))
# print(max(s))
# print()
# print(sum(l))
# soma = sum(l)
# print(soma)
# print()

# print(s)
# var1 = sorted(s) # recebe a lista já organizada em ordem crescente
# print(s)
# print(var1)

# l.extend([1,2,3])
# print(l)
# l.extend(s)
# print(l)
# print()

l = [20,10,30,50,40]
s = ["5000","Blue", "C","A", "20","Dado", "10", "Dedo","Dabura"]

# print(l)
# del l[2]
# print(l)

lista_deletados = []
print(l)
l.pop() # pop(i) remove um elemento da lista pelo índice. Quando ñão é passado um índice, por padrão remove o último elemento.
        # após remover, retorna esse elemento, que poderá ser armazenado em algum lugar
lista_deletados.append(l.pop(1)) #remove o item do índice 1 e armazena na "lista_deletados" como um novo valor com o append().
print(l)
print(lista_deletados)
lista_deletados.append(l.pop(1))
print(l)
print(lista_deletados)


# print(10 in l)
# print("Blue" in s)
# print("Goku" in s)

# if "Blue" in s:
#     print("Blue Está na lista")
# if "Goku" in s:
#     print("Goku Está na lista")

# letra = input("Digite a letra")
# if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#     print("É vogal") 
# if letra in "aeiou":
#     print("É vogal também") 
# if 10 in l:
#     print("10 está na lista")
# print()
# print(letra in "aeiou")

# print(l)
# l.reverse()
# print(l)

# print(l)
# l.append(60)
# print(l)
# l.append(int(input("Digite o novo valor: ")))
# print(l)

# ins = input("Digite o valor para insert: ")
# l.insert(3,ins) # insere um novo valor no índice especificado (não substitui, "empurra" os outros para a frente)
# print(l)
# print()


# lVazia = []
# for i in range(5):
#     lVazia.append(input("Digite um valor: "))
# print(lVazia)


### Criar uma lista a partir de um range:
L1 = list(range(1000))
print(L1)
