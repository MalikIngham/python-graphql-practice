import routes
from database import db_session, init_db
from schema import schema, Department

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
    # Base.metadata.create_all(bind=engine)
    # engineering = Department(name='Engineering')
    # db_session.add(engineering)
    # hr = Department(name='Human Resources')
    # db_session.add(hr)

    # peter = Employee(name ='peter', department=engineering)
    # db_session.add(peter)

    # roy = Employee(name ='roy', department=engineering)
    # db_session.add(roy)

    # tracy = Employee(name ='tracy', department=engineering)
    # db_session.add(tracy)

    # db_session.commit()

    return "<p>Database populated</p>"

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    init_db()
    app.run(debug=True)