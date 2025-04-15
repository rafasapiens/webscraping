import pandas as pd

tabela = pd.read_csv("obituario_marco2025.csv", sep=",")
print(tabela)

#display(tabela)
# To display the top 5 rows
tabela.head(5)

# To display the botton 5 rows
print(tabela.tail(60))

# To display types of data
print(tabela.dtypes)

# To describe data
print("Describe Data: \n",tabela.describe)

# To info data
print("Info: \n",tabela.info)

