from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite:///database.sqlite3", convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()

db = SQLAlchemy()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import Department, Employee, Role

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create the fixtures
    engineering = Department(name="Engineering")
    db_session.add(engineering)
    hr = Department(name="Human Resources")
    db_session.add(hr)

    manager = Role(name="manager")
    db_session.add(manager)
    engineer = Role(name="engineer")
    db_session.add(engineer)

    print('before peter')

    peter = Employee(name="Peter", department=engineering.department_id, role=engineer.role_id)
    db_session.add(peter)
    print(engineering.department_id)
    roy = Employee(name="Roy", department=engineering.department_id, role=engineer.role_id)
    db_session.add(roy)
    tracy = Employee(name="Tracy", department=hr.department_id, role=manager.role_id)
    print(tracy)
    db_session.add(tracy)
    # db.session.commit()
    print('finish commit')