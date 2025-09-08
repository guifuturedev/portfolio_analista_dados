
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# lendo o arquivo com os preços da gasolina
df = pd.read_csv("gasolina.csv")

# criando o gráfico de linha (dia no eixo x e preço no eixo y)
plt.figure(figsize=(8, 5))
sns.lineplot(data=df, x="dia", y="venda", marker="o")

# adicionando título e rótulos para deixar mais claro
plt.title("Preço médio da gasolina em São Paulo (Julho/2021)")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")

# salvando a imagem do gráfico em um arquivo
plt.savefig("gasolina.png")

# mostrando o gráfico na tela
plt.show() 
