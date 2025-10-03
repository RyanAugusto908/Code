def Contador_5_números():
    #Incializando positivos e negativos.
    positivo = 0
    negativo = 0
    neutro = 0

    # Para números dentro de números.
        # Digite o valor de 'numero'
        # Se numeros for maior que 0: 
            # Positivos adiciona mais 1.
        # Senão; Se numeros for menor que 0:
            # Negativos adiciona mais 1.
    for numero in range(5):
        numero = int(input(f"Digite o {numero+1}º: "))

        if numero > 0:
            positivo += 1
        elif numero < 0:
            negativo += 1
        else:
            neutro += 1

    print(f"Quantidades de números positivos: ",positivo) 
    print(f"Quantidades de números negativos: ",negativo) 
    print(f"Quantidades de números neutros: ",neutro)   

Contador_5_números()



