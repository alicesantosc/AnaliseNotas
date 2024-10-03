# Análise de Notas de Estudantes

Este projeto é uma aplicação web desenvolvida com Flask que analisa as notas de estudantes com base em dados de um arquivo CSV. A aplicação gera gráficos que ajudam a visualizar e compreender a relação entre horas estudadas e notas finais.

## Funcionalidades

- Carrega dados de um arquivo CSV contendo informações sobre horas estudadas e notas.
- Gera gráficos, incluindo:
  - Box Plot
  - Histograma
  - Scatter Plot
  - Gráfico de Linhas
  - Gráfico de Barras
  - Gráfico de Calor (Heatmap)
  - Gráfico de Pizza (Pie Chart)
- Exibe a tabela completa de dados na interface web.

## Tecnologias Utilizadas

- Python
- Flask
- Pandas
- Matplotlib
- Seaborn
- HTML/CSS (Bootstrap)

## Estrutura do Projeto

. ├── static │ └── graphs │ ├── box_plot.png │ ├── histogram.png │ ├── scatter_plot.png │ ├── line_plot.png │ ├── bar_plot.png │ ├── heatmap.png │ └── pie_chart.png ├── templates │ └── index.html ├── app.py └── requirements.txt



