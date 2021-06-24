### Criando uma função:
### Nesse momento, eu estou ensinando para o meu programa como é a função que eu quero
### Ele ainda não vai executar nada disso

### Sintaxe: def nome_da_funcao(parametros):
###              bloco de comandos

# def somar(numero1,numero2):
#     '''
#     Pede dois numeros para o usuario
#     E printa o resultado da soma dos dois
#     '''
#     soma = numero1 + numero2
#     print("A soma dos números",numero1,"e",numero2, "é:",soma)

# resposta = input("Bem vindo(a)! Gostaria de fazer uma soma?\n")
# if resposta == "sim":
#     num1 = float(input("Digite um número: "))
#     num2 = float(input("Digite outro número: "))
#     somar(num1,num2) # Nesse momento eu estou "chamando" a função, mandando o meu programa executá-la
# else:
#     print("Que pena, eu gosto tante de somar... =(")

# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno:
def area(b,a):
    terreno = b * a
    print(f"A área do terreno é: {terreno} m²")

largura = float(input("Digite a largura do terreno: "))
altura = float(input("Digite a altura do terreno: "))
area(altura,largura)  
