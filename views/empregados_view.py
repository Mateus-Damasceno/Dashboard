import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import plotly.graph_objs as go

def create_layout(dataframe, salary_data, city_data, state_data, extra_hour_data, gender_data, age_data, employee_count_data, age_gender_data):
    colors = ['#636EFA', '#EF553B', '#784315', '#DED720', '#FFA15A', '#377D22', '#EB0F04', '#B6E880', '#FF97FF', '#FECB52']
    
    age_gender_data = age_gender_data.reset_index()
    male_data = age_gender_data['M'] if 'M' in age_gender_data else [0] * len(age_gender_data)
    female_data = age_gender_data['F'] if 'F' in age_gender_data else [0] * len(age_gender_data)
    female_data = [-x for x in female_data]  # Converta os valores para negativos

    return html.Div([
        html.H1("Empregados Dashboard", style={'textAlign': 'center', 'color': '#007BFF'}),
        html.Div([
            dcc.Checklist(
                id='toggle-table',
                options=[{'label': 'Mostrar tabela', 'value': 'show'}],
                value=['show'],
                style={'margin': '20px'}
            ),
            html.Div(
                id='employee-table-container',
                children=[
                    dash_table.DataTable(
                        id='employee-table',
                        columns=[{"name": i, "id": i} for i in dataframe.columns],
                        data=dataframe.to_dict('records'),
                        page_size=10,
                        style_table={'overflowX': 'auto'},
                        style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'},
                        style_cell={'textAlign': 'left', 'padding': '5px'},
                        style_data={'border': '1px solid grey'}
                    )
                ],
                style={'display': 'block'}
            ),
        ], style={'padding': '20px'}),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='employee-graph',
                    figure={
                        'data': [
                            go.Bar(x=salary_data['Área'], y=salary_data['Total Salario'], name='Total Salario', marker=dict(color=colors)),
                        ],
                        'layout': go.Layout(
                            title='Total Salário por Área',
                            plot_bgcolor='#F9F9F9',
                            paper_bgcolor='#F9F9F9',
                        )
                    }
                ),
            ], className='three columns', style={'width': '32%', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(
                    id='extra-hour-graph',
                    figure={
                        'data': [
                            go.Bar(x=extra_hour_data['Área'], y=extra_hour_data['Total Horas Extras'], name='Total Horas Extras', marker=dict(color=colors)),
                        ],
                        'layout': go.Layout(
                            title='Horas Extras por Área',
                            plot_bgcolor='#F9F9F9',
                            paper_bgcolor='#F9F9F9',
                        )
                    }
                ),
            ], className='three columns', style={'width': '32%', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(
                    id='employee-count-graph',
                    figure={
                        'data': [
                            go.Bar(x=employee_count_data['Área'], y=employee_count_data['Count'], name='Número de Funcionários', marker=dict(color=colors)),
                        ],
                        'layout': go.Layout(
                            title='Número de Funcionários por Área',
                            plot_bgcolor='#F9F9F9',
                            paper_bgcolor='#F9F9F9',
                        )
                    }
                ),
            ], className='three columns', style={'width': '32%', 'display': 'inline-block'}),
        ], className='row', style={'padding': '20px'}),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='city-graph',
                    figure={
                        'data': [
                            go.Bar(x=city_data['Cidade'], y=city_data['Count'], name='Empregados', marker=dict(color=colors)),
                        ],
                        'layout': go.Layout(
                            title='Empregados por Cidade',
                            plot_bgcolor='#F9F9F9',
                            paper_bgcolor='#F9F9F9',
                        )
                    }
                ),
            ], className='six columns', style={'width': '48%', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(
                    id='state-graph',
                    figure={
                        'data': [
                            go.Bar(x=state_data['Estado'], y=state_data['Count'], name='Empregados', marker=dict(color=colors)),
                        ],
                        'layout': go.Layout(
                            title='Empregados por Estado',
                            plot_bgcolor='#F9F9F9',
                            paper_bgcolor='#F9F9F9',
                        )
                    }
                ),
            ], className='six columns', style={'width': '48%', 'display': 'inline-block'}),
        ], className='row', style={'padding': '20px'}),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='gender-pie-chart',
                    figure={
                        'data': [
                            go.Pie(labels=gender_data['Genero'], values=gender_data['Count'], name='Genero', marker=dict(colors=colors)),
                        ],
                        'layout': go.Layout(
                            title='Distribuição por Gênero',
                            plot_bgcolor='#F9F9F9',
                            paper_bgcolor='#F9F9F9',
                        )
                    }
                ),
            ], className='six columns', style={'width': '48%', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(
                    id='age-distribution-graph',
                    figure={
                        'data': [
                            go.Pie(labels=age_data['Faixa Etária'], values=age_data['Count'], name='Faixa Etária', marker=dict(colors=colors)),
                        ],
                        'layout': go.Layout(
                            title='Distribuição por Faixa Etária',
                            plot_bgcolor='#F9F9F9',
                            paper_bgcolor='#F9F9F9',
                        )
                    }
                ),
            ], className='six columns', style={'width': '48%', 'display': 'inline-block'}),
        ], className='row', style={'padding': '20px'}),

        html.Div([
            dcc.Graph(
                id='age-gender-pyramid',
                figure={
                    'data': [
                        go.Bar(y=age_gender_data['Faixa Etária'], x=male_data, name='M', orientation='h', marker=dict(color='blue')),
                        go.Bar(y=age_gender_data['Faixa Etária'], x=female_data, name='F', orientation='h', marker=dict(color='pink')),
                    ],
                    'layout': go.Layout(
                        title='Pirâmide Etária',
                        barmode='overlay',
                        bargap=0.1,
                        xaxis=dict(title='População', tickvals=[-max(female_data), 0, max(male_data)], ticktext=[str(max(female_data)), '0', str(max(male_data))]),
                        yaxis=dict(title='Faixa Etária'),
                        plot_bgcolor='#F9F9F9',
                        paper_bgcolor='#F9F9F9',
                    )
                }
            ),
        ], className='row', style={'padding': '20px'}),
    ], style={'backgroundColor': '#F9F9F9'})