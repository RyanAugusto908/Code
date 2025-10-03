import random
# Lista número.
numero = list(range(1,20))

# Mateus == lista que será utilizada para armazenar sublistas.
mateus = []

# Tamanho da matriz
for indice in range(4):
    vitor = random.sample(numero,5)
    mateus.append(vitor)

# Resposta
tentativa = 1
print(f"\n{tentativa}º tentativa.")    
adivinha = int(input("Adivinhe um número de 1 à 20: "))

# Em caso de acerto
encontrado = False
for indice, linha in enumerate(mateus):
    if adivinha in linha:
        print(f"O número {adivinha} está na posição: Linha {indice + 1}, Coluna {linha.index(adivinha) + 1}")
        encontrado = True

# Tentativas:        
while not encontrado:
    tentativa += 1
    print(f"\n{tentativa}º tentativa.")
    int(input(f"O número {adivinha} não foi encontrada na matriz, tente novamente: "))
    if tentativa == 3:
        print("PERDEU!!!")
        break
    
# Exibir a matriz
print("A matriz gerada com números foi:")
for linha in mateus:
    print(linha)




    
