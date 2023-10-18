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
# @app.register_blueprint(routes.main.bp, url_prefix='/main')

@app.route('/')
def hello():
    return "<p>Database populated</p>"

@app.route('/test')
def test():
    # engineering = DepartmentModel(name='Engineering')
    medical = DepartmentModel(name='Medical')
    db_session.add(medical)
    tommy = EmployeeModel(name='tommy')
    db_session.add(tommy)
    manager = RoleModel(name='manager', department_id=1)
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

@app.route('/output-departments')
def output_departments():
    payload = get_all_departments()
    # payload['departments'][1]['string']
    return payload

@app.route('/get-engineer')
def get_engineer(employee_id: int):
    try:
        engineers = EmployeeModel.query.get(employee_id).to_dict()
        print('engineers: ', engineers)

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
def all_employees():
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

@app.route('/output')
def output_engineers():
    response = get_engineer(1)
    print('response: ', response)
    return response

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    init_db()
    app.run(debug=True)