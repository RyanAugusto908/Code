linha = 1
coluna = 1

# Intervalo de 10 posições.
for linha in range(1,10):
    for coluna in range(1,3):
        if linha == 2:
            continue
        print(linha,coluna)
        
    
    # Valor 2, exibir palavra pulando.
    if linha == 2:
        print(f"--------------------\n{linha = } Pulando...\n--------------------")
        
    # Valor 8, informar 8 e parar o código.
    if linha == 8:
        print("-"*31,f"\n{linha = }. Logo não continuará.\n"+"-"*31)
        break
print("-"*23,"\nEstrutura FOR completa.\n"+"-"*23)