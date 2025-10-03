import python.formatacao as format

def test_monta_insere_livro():
    entrada = [
        "Orçamento sem falhas",
        "Nath Finanças",
        "9786555601565",
        "128",
        "2021",
        1
    ]
    
    esperado = 'INSERT INTO livros (titulo, id_autor, ano) VALUES ("Orçamento sem falhas",1,2021)'
               
    resultado = format.monta_insere_livro(entrada)
    
    assert resultado == esperado
    
def test_monta_consulta_livro():
    entrada = [
        "Orçamento sem falhas",
        "Nath Finanças",
        "9786555601565",
        "128",
        "2021",
        1
    ]
    
    esperado = 'SELECT id FROM livros WHERE titulo = ("Orçamento sem falhas")'
    
    resultado = format.monta_consulta_livro(entrada)
    
    assert resultado == esperado

def test_monta_insere_autor():
    entrada = [
        "Orçamento sem falhas",
        "Nath Finanças",
        "9786555601565",
        "128",
        "2021",
        1
    ]
    
    esperado = 'INSERT INTO autores (nome) VALUES ("Nath Finanças")'
    
    resultado = format.monta_insere_autor(entrada)
    
    assert resultado == esperado
    
def test_monta_consulta_autor():
    entrada = [
        "Orçamento sem falhas",
        "Nath Finanças",
        "9786555601565",
        "128",
        "2021",
        1
    ]
    
    esperado = 'SELECT id FROM autores WHERE nome = ("Nath Finanças")'
    
    resultado = format.monta_consulta_autor(entrada)
    
    assert resultado == esperado
    
def test_limpar_query():
    entrada = """
        SELECT
            id
        FROM
            autores
        WHERE
            nome = ("Nath Finanças")
    """
    
    esperado = 'SELECT id FROM autores WHERE nome = ("Nath Finanças")'
    
    resultado = format.limpar_query(entrada)
    
    assert resultado == esperado