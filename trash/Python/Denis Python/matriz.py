import random

# Gerar matriz 3x3 com nomes de frutas.
frutas = ["Maçã","Banana","Uva","Laranja","Pera","Manga","Abacaxi","Melancia","Morango"]
matriz = []

for i in range(3):
    vetor = random.sample(frutas,3)
    matriz.append(vetor)
    
# Exibir a matriz
print("Matriz gerada com frutas:")
for linha in matriz:
    print(linha)
    
# Verificar se uma fruta está na matriz.
fruta = input("\nDigite o nome de uma fruta para buscar na matriz: ")

encontrado = False
for i, linha in enumerate(matriz):
    if fruta in linha:
        print(f"A fruta {fruta} está na posição: Linha{i + 1}, Coluna {linha.index(fruta) + 1}")
        encontrado = True
        
if not encontrado:
    print(f"A fruta {fruta} não foi encontrada na matriz.")