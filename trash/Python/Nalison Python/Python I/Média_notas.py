aluno = str(input("Nome do aluno: "))
nota1 = float(input("1º nota: "))
nota2 = float(input("2º nota: "))
nota3 = float(input("3º nota: "))
nota4 = float(input("4º nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("Média do aluno ",aluno," é ",media,", aprovado.")
else:
    print("Média do aluno ",aluno," é ",media,", reprovado.")
    