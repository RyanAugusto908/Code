nome = input(f"\nSeu nome é: ")
idade = input("Digite sua idade: ")
print(f"\nSeu nome invertido é {nome[::-1]}") # 2 omitidos, -1 sendo para ler de direita para esquerda.

if not nome.strip or not idade.strip():
    print("Você deixou campos vazios.")

if " " in nome:
    print(f"\nO nome {nome} contem espaços.")
else:
    print(f"\nO nome {nome} não contem espaços.")
    
print(f"\nNo meu nome contem {len(nome)} caracteres.")

print(f"\nA primeira letra do nome {nome[0:1]}")

print(f"\nA ultima letra é {nome[3::]}")


