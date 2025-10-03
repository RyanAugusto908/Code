import time

def regressiva():
    
    nivel = 1
    mensagem1 = (
        """
-------------------
Contagem regressiva
-------------------
     """
     )
    mensagem2 = (f"segundo")
    
    for nivel in range(6,0,-1):                  
        print(f"{nivel*10} ==========> {mensagem1}")
        for nivel in range (9):
            print(f"{nivel+1}º - {mensagem2}")
            time.sleep(1)
    print
    (
        """
------------------
O tempo acabou!!!!
------------------
"""
)
        
regressiva()