import pandas as pd 

file = 'data/vendas.csv'

vendas = pd.read_csv(file ,encoding='utf-8', sep=',')

#print(vendas.head(5))
#print(vendas['Date'].dtypes)

vendas['Date'] = pd.to_datetime(vendas['Date'])  # Converter coluna de data para datetime

# Agregação por ano e mês
vendas['Ano'] = vendas['Date'].dt.year
vendas['Mês'] = vendas['Date'].dt.month

resumo_vendas = vendas.groupby(['Ano', 'Mês']).agg({'cogs': 'sum'}).reset_index()

#print(vendas.dtypes)
print(resumo_vendas.head(5))

exportar = 'data/resumo_vendas.xlsx'
resumo_vendas.to_excel(exportar, index=False)
#vendas.dropna(inplace=True)  # Remover valores nulos
#print(vendas.isna().any().any())