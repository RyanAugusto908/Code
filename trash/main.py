import read
#import mysql

lista_livros = read.leitura_csv("CSV\livros.csv")

for i in range(len(lista_livros)):
    query = f"insert into livro (titulo) Values {lista_livros[i][0]})"
    #consulta = mysql.executar_query(query)

#print(consulta)