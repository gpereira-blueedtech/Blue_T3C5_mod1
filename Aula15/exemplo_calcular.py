def calcular(lista , sinal= '*'):
    resultado = 1
    for i in lista:
        if sinal == "+":
            resultado += i
        elif sinal == "-":
            resultado -= i
        elif sinal == "*":
            resultado *= i
        elif sinal == "/":
            resultado /= i
        else:
            return "Operador inválido"
    return resultado

