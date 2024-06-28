import pandas as pd
from datetime import datetime

class EmployeeModel:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()
        self.data['Estado'] = self.data['Endereço'].apply(self.extract_state)
        self.data['Cidade'] = self.data['Endereço'].apply(self.extract_city)
        self.data['Idade'] = self.data['Data de Nascimento'].apply(self.calculate_age)
        self.data['Faixa Etária'] = self.data['Idade'].apply(self.categorize_age)

    def load_data(self):
        return pd.read_excel(self.file_path)

    def get_data(self):
        return self.data

    def extract_state(self, address):
        parts = address.split('-')
        if len(parts) > 2:
            state_part = parts[-2].strip()
            state = state_part.split(',')[0].strip()
            return state
        return 'Desconhecido'

    def extract_city(self, address):
        parts = address.split(',')
        if len(parts) > 2:
            city_part = parts[-2].strip()
            city = city_part.split('-')[0].strip()
            return city
        return 'Desconhecido'
    
    def get_extra_hours_by_area(self):
        return self.data.groupby('Área')['Horas Extras'].sum().reset_index(name='Total Horas Extras')
    
    def get_gender_distribution(self):
        return self.data['Genero'].value_counts().reset_index(name='Count').rename(columns={'index': 'Genero'})
    
    def calculate_age(self, birthdate):
        if isinstance(birthdate, pd.Timestamp):
            birthdate = birthdate.strftime('%m/%d/%Y')
        birthdate = datetime.strptime(birthdate, '%m/%d/%Y')
        today = datetime.today()
        return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    def categorize_age(self, age):
        if age < 25:
            return '0-25'
        elif 25 <= age < 35:
            return '25-34'
        elif 35 <= age < 45:
            return '35-44'
        elif 45 <= age < 55:
            return '45-54'
        else:
            return '55+'
        
    def get_age_distribution(self):
        return self.data['Faixa Etária'].value_counts().reset_index(name='Count').rename(columns={'index': 'Faixa Etária'})
 
    def get_total_salary_by_area(self):
        return self.data.groupby('Área')['Salario'].sum().reset_index(name = 'Total Salario')

    def get_employee_count_by_area(self):
        return self.data.groupby('Área').size().reset_index(name='Count')
    
    def get_age_gender_distribution(self):
        return self.data.groupby(['Faixa Etária', 'Genero']).size().unstack().fillna(0)