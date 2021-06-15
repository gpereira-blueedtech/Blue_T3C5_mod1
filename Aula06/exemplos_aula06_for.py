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
# range(a,b,c) -> a: número inicial da sequência

# a = input("Digite uma frase:\n")
letras_A = 0
cont = 0
# print(len(a))
print()
lista = range(5)
for i in range(0,10,4):
    print(i)
    cont += 1
    if i == "a" or i == "A":
        letras_A += 1
        print("Olha a letra A aí gente!!!")
        break
print()
print(lista)
print()
print("Contador: ")
print(cont)

# print(f"A frase tem: {letras_A} letras 'A' ")
# print("A frase tem:",letras_A,"letras 'A' ")
# Exemplo range(50) = (0,1,2,3,4,5,6....,50)
