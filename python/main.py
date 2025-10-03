import read
import transacoes
from mysql import MySQL

if __name__ == "__main__":
    livros = read.leitura_arquivo_csv("pasta_csv/livros.csv")
    
    banco_dados = MySQL("localhost","root","","biblioteca")
    banco_dados.conectar()
    
    for livro in livros:
        transacoes.inserir_livro(banco_dados, livro)
        
    banco_dados.desconectar()