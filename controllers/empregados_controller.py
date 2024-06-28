from models.empregados_model import EmployeeModel

class EmployeeController:
    def __init__(self, file_path):
        self.model = EmployeeModel(file_path)

    def get_employee_data(self):
        return self.model.get_data()

    def get_employees_by_state(self):
        data = self.model.get_data()
        return data.groupby('Estado').size().reset_index(name='Count')

    def get_employees_by_city(self):
        data = self.model.get_data()
        return data.groupby('Cidade').size().reset_index(name='Count')

    def get_total_salary_by_area(self):
        return self.model.get_total_salary_by_area()
   
    def get_extra_hours_by_area(self):
        return self.model.get_extra_hours_by_area()

    def get_gender_distribution(self):
        return self.model.get_gender_distribution()
    
    def get_age_distribution(self):
        return self.model.get_age_distribution()

    def get_employee_count_by_area(self):
        return self.model.get_employee_count_by_area()
    
    def get_age_gender_distribution(self):
        return self.model.get_age_gender_distribution()