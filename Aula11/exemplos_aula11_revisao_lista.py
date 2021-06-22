lista = ["10",10,20,30,40,50, ["Yago", ["Glauco", True]]]

for i in lista:
    print(i)

print("--==--"*5)
for i in range(len(lista)): # Crio uma sequência de número de 0 até o tamanho da lista -1
    print(i)

print("--==--"*5)
for i, v in enumerate(lista): # Retorna tanto o índice quanto o valor do elemento
    print(f'O índice {i} contém: {v}')

print("--==--"*5)
for i, v in enumerate(lista[3:],3): # Retorna a partir do item 3, e começa a contar o índice em 3
    # print(f'O índice {i} contém: {v}')
    print(i)
    print(v)