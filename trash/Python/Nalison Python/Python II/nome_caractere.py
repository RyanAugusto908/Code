"""Escreva um algoritmo que solicite o nome de um determinado usuário. Se o nome
informado tiver menos de 08 caracteres, imprima: “O seu nome tem apenas X
caracteres”. Caso tenha entre 08 e 10 caracteres, escreva “O seu nome possui uma
quantidade satisfatória de caracteres, X ”. Se o nome informado tiver mais de 10
caracteres, imprima “O seu nome é grande. Pois, possui X caracteres”. Caso o nome
não seja informado, exiba uma mensagem solicitando que o mesmo seja digitado
com no mínimo, 03 caracteres."""

def inicio():
    #Solicite o nome:
    nome = str(input("Digite seu nome: "))
    while True:
        
        if len(nome) == 0:
            nome = input(f"Digite um número com no mínimo 3 caracteres: ")
        else:
            break
    
    #Verifica se o nome tem menos de 8 caracteres:
        if len(nome) < 8:
            print(f"O seu nome tem apenas {len(nome)} caracteres.")
        elif 8 >= len(nome) < 12:
            print(f"O seu nome possui uma quantidade satisfatória de caracteres, {len(nome)}.")
        else:
            print(f"O seu nome é grande. Pois, possui {len(nome)} caracteres.")
    
inicio()