# a = 10

# if a > 5:
#     print("É maior")

# # elif a < 5:
# #     print("Não é")

# else:
#     print("É igual")


# senha = "123456"
# entrada = input("Digite a senha: ")

# if entrada == "123456":
#     print("Ok, acesso concedido.")

# elif entrada == "senhamestre":
#     print("Acesso mestre")

# else:
#     print("Senha errada")


a = int(input("Digite um número"))

if a > 10:
    print("maior que 10")
    if a > 15: # if aninhado (começa outro if, não tem a ver com o anterior, mas só entra aqui se o anterior for True)
        print("É maior que 15")
    elif a > 12: # diz respeito ao if aninhado, que está na mesma linha de indentação
        print("maior que 12")
    else: # se os demais falharem, obrigatóriamente cai aqui
        print("É 11 ou 12!")
elif a > 5: #diz respeito ao 1º if, que está na mesma linha de indentação
    print("maior que 5")
else: # se tudo falhar, cai aqui obrigatóriamente, quer você queira ou não.
    print("É menor ou igual a 5")