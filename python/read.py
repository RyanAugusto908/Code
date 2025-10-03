def leitura_arquivo_csv(nome_arquivo):
    arquivo_csv = []
    with open(nome_arquivo,"r",encoding = "utf-8") as csv:
        for linha in csv:
            arquivo_csv.append( dividir_linha(linha) )

    arquivo_csv.pop(0)
    return arquivo_csv

def dividir_linha(linha):
    return linha.strip("\n").split(";")