"""
Desenvolva um algoritmo capaz de percorrer um intervalo de 10 posições. Quando
passar pelo número 2, informar que naquele ponto a variável utilizada é 2, seguido
da palavra pulando. Ao assumir o valor 8, informar que naquele ponto a variável
utilizada é 8 e parar o código. Ao final, insira um else com a seguinte saída:
“Estrutura FOR completa”
"""
linha = 0
coluna = 0

# Intervalo de 10 posições.
for linha in range(10):
    for coluna in range(2):
        linha  += 0
        coluna += 1
        if linha == 2:
            break
        print(linha,coluna)
        
    
    # Valor 2, exibir palavra pulando.
    if linha == 2:
        print(f"--------------------\n{linha = } Pulando...\n--------------------")
        
    # Valor 8, informar 8 e parar o código.
    if linha == 8:
        print("-"*31,f"\n{linha = }. Logo não continuará.\n"+"-"*31)
        break
print("-"*23,"\nEstrutura FOR completa.\n"+"-"*23)