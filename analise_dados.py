import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv('dados_yellow_house_sushi.csv')

# Análise do horário de maior pico de vendas
df['hora_pedido'] = pd.to_datetime(df['hora_pedido'], format='%H:%M').dt.hour
horario_pico = df['hora_pedido'].value_counts().sort_index()
horario_maior_pico = horario_pico.idxmax()
total_pedidos_pico = horario_pico.max()

print('\nHorário de maior pico de vendas:')
print(f'{horario_maior_pico}:00 com {total_pedidos_pico} pedidos')

plt.figure(figsize=(10,6))
ax1 = horario_pico.plot(kind='bar', color='seagreen', edgecolor='black')
plt.title('Pedidos por Horário', fontsize=16)
plt.xlabel('Hora do Pedido', fontsize=12)
plt.ylabel('Número de Pedidos', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
# Adiciona os valores acima das barras
for i, v in enumerate(horario_pico):
	ax1.text(i, v + 0.5, str(v), ha='center', va='bottom', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('pedidos_por_horario.png')
plt.close()

import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv('dados_yellow_house_sushi.csv')


# Pratos mais vendidos (soma das quantidades)
pratos_mais_vendidos = df.groupby('prato')['quantidade'].sum().sort_values(ascending=False)

# Localidades com mais pedidos (contagem de pedidos)
localidades_mais_pedidos = df['bairro_cliente'].value_counts()


# Exibir informações numéricas detalhadas
print('--- Informações Detalhadas ---')
print('\nTop 5 pratos mais vendidos:')
print(pratos_mais_vendidos.head(5))
print('\nTotal de pratos vendidos:', pratos_mais_vendidos.sum())

print('\nTop 5 localidades com mais pedidos:')
print(localidades_mais_pedidos.head(5))
print('\nTotal de pedidos:', localidades_mais_pedidos.sum())

plt.figure(figsize=(12,7))
ax2 = pratos_mais_vendidos.plot(kind='bar', color='royalblue', edgecolor='black')
plt.title('Pratos Mais Vendidos', fontsize=16)
plt.xlabel('Prato', fontsize=12)
plt.ylabel('Quantidade Vendida', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
# Adiciona os valores acima das barras
for i, v in enumerate(pratos_mais_vendidos):
	ax2.text(i, v + 0.5, str(v), ha='center', va='bottom', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('pratos_mais_vendidos.png')
plt.close()

plt.figure(figsize=(12,7))
ax3 = localidades_mais_pedidos.plot(kind='bar', color='darkorange', edgecolor='black')
plt.title('Localidades com Mais Pedidos', fontsize=16)
plt.xlabel('Bairro', fontsize=12)
plt.ylabel('Número de Pedidos', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
# Adiciona os valores acima das barras
for i, v in enumerate(localidades_mais_pedidos):
	ax3.text(i, v + 0.5, str(v), ha='center', va='bottom', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('localidades_mais_pedidos.png')
plt.close()

print('\nOs gráficos foram salvos como pratos_mais_vendidos.png e localidades_mais_pedidos.png na pasta do projeto.')
