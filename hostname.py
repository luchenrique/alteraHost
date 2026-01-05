import pandas as pd

arquivo_entrada = 'host.csv'
arquivo_saida = 'hostnames_formatados.csv'
nome_coluna = 'hostname' 

try:
    df = pd.read_csv(arquivo_entrada)

    df[nome_coluna] = 'PD1-' + df[nome_coluna].astype(str)

    df.to_csv(arquivo_saida, index=False)
    
    print(f"Sucesso! Arquivo '{arquivo_saida}' gerado.")
    print(df.head()) 

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")
except KeyError:
    print(f"Erro: A coluna '{nome_coluna}' não existe no arquivo CSV.")