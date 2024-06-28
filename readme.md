# Employee Dashboard

## Descrição do Projeto

O Employee Dashboard é uma aplicação web interativa desenvolvida com Dash, uma framework de código aberto baseada no Flask, Plotly e React.js. Esta aplicação permite visualizar e analisar dados de funcionários a partir de um arquivo Excel. O dashboard exibe várias métricas e gráficos, incluindo distribuição de funcionários por área, cidade, estado, gênero e faixa etária, além de horas extras e salários.

## Funcionalidades

- **Tabela de Dados:** Visualize uma tabela interativa com os dados dos funcionários.
- **Gráficos de Barras:** Exibe o total de salários, horas extras e número de funcionários por área.
- **Gráficos de Barras:** Mostra a distribuição de funcionários por cidade e estado.
- **Gráfico de Pizza:** Apresenta a distribuição de funcionários por gênero e faixa etária.
- **Pirâmide Etária:** Visualiza a distribuição de funcionários por faixa etária e gênero.

## Estrutura do Projeto

O projeto é dividido em três componentes principais:

1. **Model:** `EmployeeModel` é responsável por carregar, processar e manipular os dados do arquivo Excel.
2. **Controller:** `EmployeeController` interage com o `EmployeeModel` para obter os dados processados necessários para a visualização.
3. **View:** Define o layout e os gráficos utilizando componentes do Dash.

## Dependências

- `pandas`
- `dash`
- `dash-core-components`
- `dash-html-components`
- `dash-table`
- `plotly`

## Uso
Execute a aplicação:

1. python app.py
2. Abra um navegador web e vá para http://127.0.0.1:8050/ para visualizar o dashboard.

## Estrutura do Código

**models/empregados_model.py**: Contém a classe EmployeeModel que carrega e processa os dados dos funcionários.
**controllers/empregados_controller.py**: Contém a classe EmployeeController que interage com o modelo para obter os dados processados.
**views/empregados_view.py**: Define o layout e os gráficos do Dash.
**app.py**: Arquivo principal que inicializa a aplicação Dash e configura os callbacks para interatividade.

## Funcionalidades Detalhadas

EmployeeModel

- __init__(file_path): Inicializa o modelo e carrega os dados do arquivo Excel.
- load_data(): Carrega os dados do arquivo Excel.
- extract_state(address): Extrai o estado do endereço.
- extract_city(address): Extrai a cidade do endereço.
- calculate_age(birthdate): Calcula a idade a partir da data de nascimento.
- categorize_age(age): Categoriza a idade em faixas etárias.
- get_extra_hours_by_area(): Obtém o total de horas extras por área.
- get_gender_distribution(): Obtém a distribuição de gênero.
- get_age_distribution(): Obtém a distribuição por faixa etária.
- get_total_salary_by_area(): Obtém o total de salários por área.
- get_employee_count_by_area(): Obtém o número de funcionários por área.
- get_age_gender_distribution(): Obtém a distribuição de funcionários por faixa etária e gênero.

EmployeeController

- get_employee_data(): Retorna os dados dos funcionários.
- get_employees_by_state(): Retorna o número de funcionários por estado.
- get_employees_by_city(): Retorna o número de funcionários por cidade.
- get_total_salary_by_area(): Retorna o total de salários por área.
- get_extra_hours_by_area(): Retorna o total de horas extras por área.
- get_gender_distribution(): Retorna a distribuição de gênero.
- get_age_distribution(): Retorna a distribuição por faixa etária.
- get_employee_count_by_area(): Retorna o número de funcionários por área.
- get_age_gender_distribution(): Retorna a distribuição por faixa etária e gênero.
- create_layout: Define o layout e os gráficos do Dash utilizando os dados processados pelo EmployeeController.