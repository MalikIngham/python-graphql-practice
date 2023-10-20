import routes
import models
from database import db_session, init_db
from schema import schema, DepartmentModel, EmployeeModel, RoleModel

from flask import Flask
from flask_graphql import GraphQLView


app = Flask(__name__)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
        )
)   

@app.route('/')
def hello():
    return "<p3>Hello</p3>"

@app.route('/test')
def test():
    medical = DepartmentModel(name='Medical')
    medical.department_id = 3
    db_session.add(medical)
    manager = RoleModel(name='manager', department_id=medical.department_id)
    db_session.add(manager)
    db_session.commit()

    return 'TEST'

@app.route('/get-all-departments')
def get_all_departments():
    try:
        departments = [dept.to_dict() for dept in DepartmentModel.query.all()]
        payload = {
            'success': True,
            'departments': departments
        }
    except Exception as error:
        payload = {
            'success': False,
            'errors': [str(error)]
        }

    return payload

@app.route('/departments')
def output_departments():
    try:
        departments = DepartmentModel.query.all()
        response = {
            'success': True,
            'departments': departments.to_dict()
        }
    except Exception as error:
        response = {
            'success': False,
            'error': [str(error)]
        }
    return response

@app.route('/engineer/<int:employee_id>')
def get_engineer(employee_id: int):
    try:
        engineers = EmployeeModel.query.get(employee_id).to_dict()
        response = {
            'success': True,
            'engineers': engineers
        }

    except Exception as error:
        response = {
            'success': False,
            'error': [str(error)]
        }

    return response

@app.route('/get-all-employees')
def get_all_employees():
    '''Retrieving all employees'''
    try: 
        employees = [employee.to_dict() for employee in EmployeeModel.query.all()]
        response = {
            'success': True,
            'employee': employees
        }
    except Exception as error:
        response = {
            'success': False,
            'error': [str(error)]
        }

    return response

@app.route('/department/<int:department_id>')
def get_department(department_id):
    '''Retrieving a specific department by department_id using GraphQL'''
    try:
        department = DepartmentModel.query.get(department_id).to_dict()
        response = {
            'success': True,
            'department': department
        }
    except Exception as error:
        response = {
            'success': False,
            'error': [str(error)]
        }

    return response

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    init_db()
    app.run(debug=True)