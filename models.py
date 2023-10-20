from database import Base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import backref, relationship

db = SQLAlchemy()


class Department(Base):
    __tablename__ = "department"
    department_id = db.Column(Integer, primary_key=True)
    name = db.Column(String)

    # employee = db.relationship('Employee')

    def __repr__(self) -> str:
        # return "<Department(name='%s')>" %(
        #     self.name
        # )
    
        return f'<Department: (name={self.name})>'
    
    def to_dict(self):
        '''Converts class model to dictionary'''
        return {
            "department_id": self.department_id,
            "string": self.name
        }


class Role(Base):
    __tablename__ = "roles"
    role_id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    department_id = db.Column(Integer, db.ForeignKey("department.department_id"))
    department = db.relationship('Department', backref='roles')

    def __repr__(self) -> str:
        return f'<Role(name= {self.name}, department ID = {self.department_id})>'
    
    def to_dict(self):
        '''Converts class model to dictionary'''
        return {
            'role_id' : self.role_id,
            'name': self.name,
            'department_id': self.department_id,
            'department': self.department.to_dict() if self.department else [],
        }


class Employee(Base):
    __tablename__ = "employee"
    employee_id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    # Use default=func.now() to set the default hiring time
    # of an Employee to be the current time when an
    # Employee record was created
    hired_on = db.Column(DateTime, default=func.now())
    department_id = db.Column(Integer, ForeignKey("department.department_id"))
    role_id = db.Column(Integer, ForeignKey("roles.role_id"))
    # Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
    # department = relationship(
    #     Department, backref=backref("employees", uselist=True, cascade="delete,all")
    # )

    department = db.relationship('Department', backref='employee')
    role = db.relationship('Role', backref='employee')

    def __repr__(self) -> str:
        return f'<Employee(name={self.name}, hired_on = {self.hired_on}, department_id={self.department_id}, role_id={self.role_id})>'
    
    def to_dict(self):
        '''Converts class model to dictionary'''
        print(self.role)
        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'hired_on': self.hired_on,
            'role': self.role.to_dict() if self.role else [],
            'department': self.department.to_dict() if self.department else [],
        }