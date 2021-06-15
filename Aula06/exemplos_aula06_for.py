### While: enquanto uma condição for verdadeira, repita:

# senha = "Blue123"
# entrada = input("Digite sua senha: ")
# erros = 0
# while senha != entrada:
#     erros += 1
#     entrada = input("Senha incorreta!! \nDigite novamente: ")
#     if entrada == senha:
#         print("Bem vindo")
#     if erros == 5:
#         print("Tentativas esgotadas!")
#         break

# print(f"VocÊ errou {erros} vezes")



# For: laço de repetição que vai percorrer cada item de uma sequência
# range(a,b,c) -> a: número inicial da sequência, b: número final (-1), c: incremento (quantidade de números que vai "pular")
# range(50) -> cria uma sequência de 0 até 49
# range(10,20) -> cria uma sequência de 10 até 19
# range(1,20,2) -> cria sequência de 1 até 19, pulando e 2 em 2
# Exemplo range(50) = (0,1,2,3,4,5,6....,50)


# a = input("Digite uma frase:\n")
# letras_A = 0
# cont = 0

# for i in a:
#     print(i)
#     cont += 1
#     if i == "a" or i == "A":
#         letras_A += 1
#         print("Olha a letra A aí gente!!!")
#         break
# print()
# print("Contador: ")
# print(cont)
# print(f"A frase tem: {letras_A} letras 'A' ")
## print("A frase tem:",letras_A,"letras 'A' ") -> alternativa

lista = [10,20,30,40,50,"Blue","Rafael"]
print(len(lista))
print(lista)
print(type(lista))
print()
# print(lista[0]) -> printa o elemento do índice passado de uma lista
# print(lista[6])

for i in range(len(lista)):
    print(i)
print()

for i in lista:
    print(i)
print()
# for i in range(7):
#     print(i,lista[i])
# print()

for i in range(len(lista)):
    print(i,lista[i])
print()
# for i in lista:
#     print(i)
