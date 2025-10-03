import random
import time

# Definição das tuplas com números para a tabuada
numeros = tuple(range(1, 11))   # Tupla contando números de 1 a 10.

# Inicializando contadores
total_questoes = 10
acertos = 0

boas_vindas = "\nBem-vindo ao Quiz da Tabuada! Você precisa acertar pelo menos 70% para ser aprovado.\n"
print(boas_vindas)

# Iniciando o cronômetro.
tempo_inicio = time.time()

# Gerando 10 questões aleatórias.
for i in range(1, total_questoes + 1):
    num1 = random.choice(numeros)
    num2 = random.choice(numeros)
    resposta_correta = num1 * num2
    
    resposta_usuario = int(input(f"Questão {i}: Quanto é {num1} X {num2}?\n"))

    # Verifica se a resposta está correta:
    if resposta_usuario == resposta_correta:
        print("Correto!\n")
        acertos += 1
    else:
        print(f"Errado! A resposta correta é: {resposta_correta}")
    
# Parando o cronômetro:
tempo_fim = time.time()
tempo_total = tempo_fim - tempo_inicio

# Calculando a procentagem de acertos:
porcentagem_acertos = (acertos / total_questoes) * 100

# Verificando se o usuário foi aprovado ou reprovado:
if porcentagem_acertos >= 70:
    print(f"Parabéns! Você acertou {acertos} de {total_questoes} questões ({porcentagem_acertos:.2f}%) e foi APROVADO!")
else:
    print(f"Que pena! Você acertou {acertos} de {total_questoes} questões ({porcentagem_acertos:.2f}%) e foi reprovado.")
    
print(f"Tempo total para completar o quiz: {tempo_total:.2f} segundos")