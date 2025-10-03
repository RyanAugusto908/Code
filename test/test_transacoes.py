import python.transacoes as TR
from python.mysql import MySQL

def test_inserir_livro():
    entrada = [
        "As lições do Mestre",
        "Nath Finanças",
        "9786555601565",
        "128", 
        "2021"
    ]
    
    banco = MySQL() 
    banco.conectar()
    
    TR.inserir_livro(banco, entrada)
    
    resultado = TR.consultar_livro(banco, entrada)
    
    assert len(resultado) > 0