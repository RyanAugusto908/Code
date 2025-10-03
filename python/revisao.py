def variaveis():
    a = 10
    print("a: ", a, type(a))

    o_valor_com_tipo_string = str(5)
    print("b: ", o_valor_com_tipo_string, type(o_valor_com_tipo_string))


def lista():
    a = [1,2,3]
    a.append(4)
    a.append(5)
    print(a, type(a), len(a))


def lista_dicionario():
    a = {
        "nome": "Joaquim",
        "idade": 81,
        "parentes": ["Maria", "Juciene", "Sebastiana"]
    }

    print(a, type(a))
    print(a["parentes"][2])


def aprovacao():
    numero_escolhido = int(input("Digite a nota do aluno número de 0 a 9\n"))

    if numero_escolhido >= 7:
        print("Você foi aprovado com: ", numero_escolhido)
    elif numero_escolhido >= 5:
        print("Você foi para a recuperção com: ", numero_escolhido)
    else:
        print("Você foi reprovado com: ", numero_escolhido)


def aprovacoes():
    for i in range(3):
        print(i)
        aprovacao()
