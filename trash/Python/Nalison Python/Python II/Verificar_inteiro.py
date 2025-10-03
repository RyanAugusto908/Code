"""
Desenvolva um algoritmo capaz de solicitar ao usuário um número inteiro. Em
seguida, verifique se o número digitado é par ou ímpar. Caso o usuário não digite
um número inteiro, exiba a seguinte mensagem “O dado informado não é um
número inteiro”.
"""
def inicio():
    # Solicitar número inteiro;
    numero = input("Digite um número inteiro: ")
    # Verificar se o número é inteiro como comando 'isdigit' e também permitir número negativo com o .lstrip:
    if numero.lstrip('-').isdigit():
        numero = int(numero)
        print(f"O número {numero} é inteiro.")
        # Número par ou impar.
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é impar.")
    else:
        print("O dado informado não é um número inteiro")
        
inicio()