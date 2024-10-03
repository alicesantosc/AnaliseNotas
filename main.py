import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path= 'C:\\Users\\alice\\Downloads\\archive\\Student_Grades.csv'
df = pd.read_csv(file_path)

sns.set(style="whitegrid")

print("Dados da Planilha")
df.columns = ['Horas_Estudadas', 'Pontos_Praticas', 'Pontos_Equipe', 'Nota_Intermediaria', 'Nota_Final', 'Pontuacao_Total', 'Nota_Final_Grade']
print(df)


plt.figure(figsize=(10, 6))
sns.barplot(x='Horas_Estudadas', y='Pontuacao_Total', data=df, palette='viridis')
plt.title('Comparação entre Horas Estudadas e Pontuação Total')
plt.xlabel('Horas Estudadas')
plt.ylabel('Pontuação Total')
plt.show()

sns.boxplot(x='Nota_Final', data=df)

# Adicionar título e rótulo do eixo
plt.title('Box Plot das Notas Finais dos Estudantes')
plt.xlabel('Notas Finais')

plt.show()