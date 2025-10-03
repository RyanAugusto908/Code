"""
A organização mundial de saúde adotou algumas regras para o cálculo da
massa corporal, definindo o peso ideal. Para que o cálculo seja realizado de
maneira correta os seguintes dados devem ser informados: peso e altura. A
seguir, tabela base para o desenvolvimento de um algoritmo capaz de calcular
o IMC conforme dados informados(peso e altura):
"""
nome = str(input("Digite seu nome: "))
peso = float(input("Seu peso: "))
altura = float(input("Sua altura: "))
imc = peso/(altura*altura)

print("Seu imc é: ",imc,)

if imc < 18.5:
    print("Portanto é menor que 18,5: Abaixo do peso")
elif imc <= 18.5 and 24.9:
    print("Portanto está entre 18,5 e 24,9: Peso normal")
elif imc <= 29.9:
    print("Portanto está entre 25,0 e 29,9: Sobrepeso")
elif imc <= 39.9:
    print("Portanto está entre 30,0 e 39,9: Obesidade")
else:
    print("Portanto está maior que 40,0: Obesidade Grave")

