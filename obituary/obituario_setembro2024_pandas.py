import pandas as pd

tabela = pd.read_csv("obituario_setembro2024.csv", sep=",")
print(tabela)

#display(tabela)
# To display the top 5 rows
tabela.head(5)

# To display the botton 5 rows
print(tabela.tail(60))

# To display types of data
print(tabela.dtypes)
