
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')
sns.set(style="whitegrid")
plt.figure(figsize=(8,5))
sns.lineplot(data=df, x='dia', y='venda', marker='o', color='blue', label='Preço da gasolina')
plt.title("Preço médio da gasolina em SP (Julho 2021)", fontsize=14)
plt.xlabel("Dia", fontsize=12)
plt.ylabel("Preço (R$)", fontsize=12)
plt.legend(title='Legenda')
plt.xticks(df['dia'])
plt.savefig("gasolina.png")
