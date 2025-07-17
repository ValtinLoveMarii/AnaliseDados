#AULA SOBRE OS PANDAS

"""LEITURA DE DADOS"""
import pandas as pd

"""LER UM ARQUIVO EXCEL E CSV"""
variavel = pd.read_excel('meu_arquivo.xlsx')

"""CRIAR O DATAFRAMe"""
dataframe = [[1, 'Joao', 'SP'], [2, 'Coringa', 'RJ']]
df1 = pd.DataFrame(dataframe, columns=['id', 'nome', 'Cidade'])

# ou ASSIM
dados = {'id':[9,0,8],'nome':['Valor1', 'Valor2', 'Valor3']}
df2 = pd.DataFrame(dados)



"""ESCREVER/CRIAR EXCEL E CSV"""
df1.to_excel('novo_arquivo.xlsx', index=True)