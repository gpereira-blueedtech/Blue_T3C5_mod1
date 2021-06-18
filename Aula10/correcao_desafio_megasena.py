# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.

# O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.


from random import randint # Importei apenas a função que vou usar, randint
# import random # -> importo a biblioteca inteira, com todas as funções

q_jogos = int(input("Quantos jogos você quer gerar?"))
jogos_total = []

for i in range(q_jogos): # Repita tantas vezes (quantidade de jogos entrada)
    jogo = list()    
    while len(jogo) < 6: # Enquanto minha lista for menor que 6, repito o bloco:
        num = randint(1, 60) # Quando importo funções específicas de uma biblioteca
        # num = random.randint(1, 60) # -> vou usar no caso de ter importado a biblioteca random inteira
        if num not in jogo: # Só armazeno o número se não estiver na lista
            jogo.append(num) # Coloca o que estiver armazenado em num no final da minha lista
    jogo.sort()
    jogos_total.append(jogo)
    
 
print("\U0001F340 Aqui estão os jogos, BOA SORTE!")

# contador = 1
# for j in jogos_total:
#     print(f"Jogo {contador}: {j}")
#     contador += 1

# Método alternativo:

for i in range(len(jogos_total)):
    print(f"Jogo {i+1}: {jogos_total[i]}")
