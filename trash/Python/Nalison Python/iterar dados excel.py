import pandas as pd
from openpyxl import load_workbook

def calcular_imc (peso,altura):
    return round(peso / (altura**2),2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso."
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"
    
# Nome do arquivo da planilha:
arquivo = "excel_teste.xlsx"

try:
    # Ler a planilha e remover espaços extras nos nomes das colunas.
    dados = pd.read_excel(arquivo)
    dados.columns = dados.columns.astype(str).str.strip()
    
    # Verificar se as colunas necessárias existem
    if not {"nome","peso","altura"}.issubset(dados.columns):
        print("O arquivo Excel deve conter as colunas: nome, peso e altura.")
    else:
        # Converter para valores numéricos (evia erro com texto)
        dados["peso"] = pd.to_numeric(dados["peso"], errors="coerce")
        dados["altura"] = pd.to_numeric(dados["altura"],errors="coerce")
        
        # Remover linhas com valores inválidos:
        dados = dados.dropna(subset=["peso","altura"])
        
        # Calcular imc e classificação:
        dados["IMC"] = dados.apply(lambda x: calcular_imc(x["peso"],x["altura"]),axis = 1)
        dados["Classificação"] = dados["IMC"].apply(classificar_imc)
        
        # Sobrescrever a planilha original mantendo os dados e adicionando as colunas novas:
        with pd.ExcelWriter(arquivo,engine="openpyxl",mode="w") as writer:
            dados.to_excel(writer,sheet_name="Pessoas",index=False)
            
        print(f"Resultados adicionados ao arquivo '{arquivo}'.")
        
except FileNotFoundError:
    print(f"Erro: Arquivo '{arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    

        
        
        
        
        