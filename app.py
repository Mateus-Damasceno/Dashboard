import dash
from dash.dependencies import Input, Output
from controllers.empregados_controller import EmployeeController
from views.empregados_view import create_layout

# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Caminho para o arquivo Excel
file_path = 'BaseFuncionarios.xlsx'

# Inicializar o controlador
controller = EmployeeController(file_path)

# Obter os dados dos funcionários
employee_data = controller.get_employee_data()
state_data = controller.get_employees_by_state()
city_data = controller.get_employees_by_city()
extra_hour_data = controller.get_extra_hours_by_area()
gender_data = controller.get_gender_distribution()
age_data = controller.get_age_distribution()
salary_data = controller.get_total_salary_by_area()
employee_count_data = controller.get_employee_count_by_area()
age_gender_data = controller.get_age_gender_distribution()

# Configurar o layout do aplicativo
app.layout = create_layout(employee_data, salary_data, city_data, state_data, extra_hour_data, gender_data, age_data, employee_count_data, age_gender_data)

# Adicionar callbacks para interatividade
@app.callback(
    Output('employee-table-container', 'style'),
    [Input('toggle-table', 'value')]
)
def toggle_table_visibility(toggle_value):
    if 'show' in toggle_value:
        return {'display': 'block'}
    return {'display': 'none'}

# Executar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)