#AULA SOBRE OS PANDAS

import pandas as pd

"""CRIAR UM DATAFRAME(TABELA)"""
dataframe = pd.DataFrame() # --> CRIA UM DATAFRAME(TABELA) EM BRANCO


#criar um dataframe apartir de um dicionario!

dicionario = {
    'data':['12/02/2025', '16/02/2025'],
    'valor':[500, 300],
    'produto':['skin', 'picareta'],
    'qtd':[40, 90]
}

# dicionario_df = pd.DataFrame(dicionario)
# print(dicionario_df)


#LER UMA BASE DE DADOS EXCEL E IMPORTA PARA O DATAFRAME

valores_arquivo = pd.read_excel('meu_arquivo.xlsx')
print(valores_arquivo)

# print(valores_arquivo.head(2)) # --> MOSTRA O TANTO DE LINHA PASSADO ALI
# print(valores_arquivo.shape) # --> MOSTRA O NUMERO DE LINHAS E COLUNAS
# print(valores_arquivo.describe()) # --> MOSTAR UM RESUMO SOBRE OS DADOS NUMERICOS DA TABELA

# print(valores_arquivo)
#EDITAR A TABELA
# valores_arquivo = valores_arquivo['Idade']

var = valores_arquivo.loc[valores_arquivo['Nome'] == 'Maria', ['Sexo']]
print(var)
