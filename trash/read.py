def leitura_csv(nome_arquivo):
    arquivo_csv = abrir_arquivo_csv(nome_arquivo)
    arquivo_dividido = dividir_arquivos(arquivo_csv)

    return arquivo_dividido


def abrir_arquivo_csv(nome_arquivo):
    arquivo_csv = []

    with open(nome_arquivo, "r", encoding="utf-8") as csv:
        for line in csv:
            arquivo_csv.append(line)

    return arquivo_csv


def dividir_arquivos(arquivo_csv):
    arquivo_dividido = []
    for linha in arquivo_csv:
        linha_dividida = dividir_linha(linha)
        arquivo_dividido.append(linha_dividida)
    
    return arquivo_dividido


def dividir_linha(linha):
    linha_dividida = linha.strip("\n").split(";")

    return linha_dividida
