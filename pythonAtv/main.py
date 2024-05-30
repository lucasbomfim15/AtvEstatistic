import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'C:/Users/Lucas/Downloads/base alunos (1).xlsx'  # Aqui ficará o caminho do arquivo!
df = pd.read_excel(file_path)


df_filtered = df[['Nota_Teste', 'TipoEsc']]

df_filtered = df_filtered.dropna()


descriptive_stats = df_filtered.groupby('TipoEsc').describe()
print("Estatísticas Descritivas:")
print(descriptive_stats)


sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.boxplot(x='TipoEsc', y='Nota_Teste', data=df_filtered)
plt.title('Distribuição das Notas por Tipo de Escola')
plt.xlabel('Tipo de Escola')
plt.ylabel('Nota do Teste')
plt.show()


notas_priv = df_filtered[df_filtered['TipoEsc'] == 'priv']['Nota_Teste']
notas_pub = df_filtered[df_filtered['TipoEsc'] == 'pub']['Nota_Teste']


t_stat, p_value = ttest_ind(notas_priv, notas_pub, equal_var=False)
print(f'T-statistic: {t_stat}, P-value: {p_value}')


alpha = 0.05
if p_value < alpha:
    print("Rejeitamos a hipótese nula. Existe uma diferença significativa entre as notas de escolas públicas e privadas.")
else:
    print("Não rejeitamos a hipótese nula. Não existe uma diferença significativa entre as notas de escolas públicas e privadas.")
