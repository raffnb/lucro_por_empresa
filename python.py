import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados de exemplo
data = {
    'Empresa': ['A', 'B', 'C', 'D'],
    'Receita': [10000, 15000, 7000, 12000],
    'Despesa': [5000, 8000, 3000, 6000]
}
df = pd.DataFrame(data)

# Calcular lucro
df['Lucro'] = df['Receita'] - df['Despesa']

# Plotar gráfico
plt.bar(df['Empresa'], df['Lucro'])
plt.xlabel('Empresa')
plt.ylabel('Lucro')
plt.title('Lucro por Empresa')
plt.savefig('lucro_por_empresa.png')
plt.show()
