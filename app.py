from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Ler o arquivo CSV
    file_path = 'C:\\Users\\alice\\Downloads\\archive\\Student_Grades.csv'
    df = pd.read_csv(file_path)
    df.columns = ['Horas_Estudadas', 'Pontos_Praticas', 'Pontos_Equipe', 'Nota_Intermediaria', 'Nota_Final',
                  'Pontuacao_Total', 'Nota_Final_Grade']

    # Criar um box plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Nota_Final', data=df)
    plt.title('Box Plot das Notas Finais dos Estudantes')
    plt.xlabel('Notas Finais')

    # Salvar o gráfico do box plot na pasta static/graphs
    box_plot_path = os.path.join('static', 'graphs', 'box_plot.png')
    plt.savefig(box_plot_path)
    plt.close()  # Fecha a figura para evitar sobreposições

    # Criar um histograma para Horas Estudadas e Nota Final
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='Horas_Estudadas', hue='Nota_Final', multiple='stack', kde=True)
    plt.title('Histograma das Horas Estudadas e Notas Finais')
    plt.xlabel('Horas Estudadas')
    plt.ylabel('Frequência')

    # Salvar o gráfico do histograma na pasta static/graphs
    hist_plot_path = os.path.join('static', 'graphs', 'histograma_horas_estudadas.png')
    plt.savefig(hist_plot_path)
    plt.close()  # Fecha a figura para evitar sobreposições


    ###
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Horas_Estudadas', y='Nota_Final', data=df)
    plt.title('Relação entre Horas Estudadas e Nota Final')
    plt.xlabel('Horas Estudadas')
    plt.ylabel('Nota Final')

    scatter_plot_path = os.path.join('static', 'graphs', 'scatter_plot.png')
    plt.savefig(scatter_plot_path)
    plt.close()

    ###
    grade_categories = pd.cut(df['Nota_Final'], bins=[0, 5, 7, 10], labels=['Baixa', 'Média', 'Alta'])
    grade_distribution = grade_categories.value_counts()

    plt.figure(figsize=(10, 6))
    plt.pie(grade_distribution, labels=grade_distribution.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição de Notas dos Estudantes')
    pie_chart_path = os.path.join('static', 'graphs', 'pie_chart.png')
    plt.savefig(pie_chart_path)
    plt.close()


    # Converter DataFrame para HTML
    table_html = df.to_html(classes='table table-striped table-bordered', index=False)


    return render_template('index.html', box_plot_path=box_plot_path, hist_plot_path=hist_plot_path,
                           table_html=table_html, scatter_plot_path=scatter_plot_path, pie_chart_path=pie_chart_path)



if __name__ == '__main__':
    app.run(debug=True)
