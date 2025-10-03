import re
  
def monta_insere_livro (livro):
    query = f"""
        INSERT INTO livros
            (titulo, id_autor, ano)
        VALUES
            ("{livro[0]}",{livro[5]},{livro[4]})
            
    """
    query = limpar_query(query)
    return query
    
def monta_consulta_livro (livro):
    query = f"""
        SELECT
            id
        FROM
            livros
        WHERE
            titulo = ("{livro[0]}")
    """
    query = limpar_query(query) 
    return query   

def monta_insere_autor(livro):
    query = f"""
        INSERT INTO 
            autores
                (nome)
        VALUES
            ("{livro[1]}")
    """
    query = limpar_query(query)
    return query

def monta_consulta_autor(livro):
    query = f"""
        SELECT
            id
        FROM
            autores
        WHERE
            nome = ("{livro[1]}")
    """
    query = limpar_query(query)
    return query
        
def limpar_query(query):
    query_limpa = re.sub(r'\s+',' ', query).strip()
    return query_limpa