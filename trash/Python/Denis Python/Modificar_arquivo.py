# Exemplo de manipulação de arquivos com open() e with statement

# Criando e escrevendo em um arquivo usando open():
file = open("exemplo.txt","w")  # O "w" significa escrita.
file.write("Este é um exemplo de manipulação de arquivos usando open().\n")
file.write("Lembre-se de sempre fechar o arquivo para evitar problemas.\n")
file.close()    # Fechando o arquivo.

# Abrindo e lendo o arquivo
file = open("exemplo.txt","r")  # "r" indica modo de leitura.
conteudo = file.read()
print("Conteúdo usando open(): ",conteudo)
file.close()    # Feche sempre o arquivo após o uso.

#Usando "with" para manipular arquivos de forma mais segura.
with open("exemplo_with.txt","w") as file:
    file.write("Este é um exemplo de manipulação segura usando 'with'.\n")
    file.write("A vantagem do 'with' é que ele fecha automaticamente o arquivo.\n")

with open("exemplo_with.txt","r") as file:
    conteudo = file.read()
    print("Conteúdo usando with statement: ",conteudo)

# Explicações:
# - open() é usado para abrir um arquivo, mas requer que você lembre de fechar o arquivo manualmente com file.close().
# - with statement é a forma mais segura, pois ela fecha automaticamente o arquivo mesmo se ocorrerem erros no meio da execução.