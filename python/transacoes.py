from python.mysql import MySQL
import python.formatacao as formatacao

def inserir_livro(banco=MySQL, livro=[]):
    titulo = consultar_livro (banco, livro)
    
    if len(titulo) == 0:
        id_autor = inserir_autor(banco, livro)
        livro.append(id_autor)
        query = formatacao.monta_insere_livro(livro)        
        banco.executar_query(query)
             
def consultar_livro(banco=MySQL, livro=[]):
    query = formatacao.monta_consulta_livro(livro)
    titulo = banco.executar_query(query)
    return titulo

def inserir_autor(banco=MySQL, livro=[]):
    autor = consultar_autor(banco, livro)
    if len(autor) > 0:
        id_autor = autor[0]["id"]
    else:
        query = formatacao.monta_insere_autor(livro)
        
        id_autor = banco.executar_query(query)
    return id_autor

def consultar_autor(banco=MySQL, livro=[]):
    query = formatacao.monta_consulta_autor(livro)
    autor = banco.executar_query(query)
    return autor
        
  