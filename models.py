from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import backref, relationship


class Department(Base):
    __tablename__ = "department"
    department_id = Column(Integer, primary_key=True)
    name = Column(String)

    employee = relationship('Employee', primaryjoin= 'Employee.department_id == foreign(Department.department_id)')

    def __repr__(self) -> str:
        # return "<Department(name='%s')>" %(
        #     self.name
        # )
    
        return f'<Department(name={self.name})>'
    
    def to_dict(self):
        '''Converts class model to dictionary'''
        return {
            "department_id": self.department_id,
            "string": self.name
        }


class Role(Base):
    __tablename__ = "roles"
    role_id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey("department.department_id"))
    department = relationship(
        'Department', primaryjoin='Role.department_id == foreign(Department.department_id)',
        # backref=backref("employees", uselist=True, cascade="delete,all"
        #                 )
    )
    
    def __repr__(self) -> str:
        return f'<Role(name={self.name}, department_id={self.department_id})>'
    
    def to_dict(self):
        '''Converts class model to dictionary'''
        return {
            'role_id' : self.role_id,
            'name': self.name,
            'department_id': self.department_id,
            'department': self.department
        }


class Employee(Base):
    __tablename__ = "employee"
    employee_id = Column(Integer, primary_key=True)
    name = Column(String)
    # Use default=func.now() to set the default hiring time
    # of an Employee to be the current time when an
    # Employee record was created
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey("department.department_id"))
    role_id = Column(Integer, ForeignKey("roles.role_id"))
    # Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
    # department = relationship(
    #     Department, backref=backref("employees", uselist=True, cascade="delete,all")
    # )
    department = relationship(
        'Department', primaryjoin='Employee.department_id == foreign(Department.department_id)',
        # backref=backref("employees", uselist=True, cascade="delete,all"
        #                 )
    )

    role = relationship(
        'Role', primaryjoin='Employee.role_id == foreign(Role.role_id)',
        # backref=backref("employees", uselist=True, cascade="delete,all"
        #                 )
    )
    # role = relationship(
    #     Role, backref=backref("roles", uselist=True, cascade="delete,all")
    # )

    def __repr__(self) -> str:
        return f'<Employee(name={self.name}, hired_on = {self.hired_on}, department_id={self.department_id}, role_id={self.role_id})>'
    
    def to_dict(self):
        '''Converts class model to dictionary'''
        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'hired_on': self.hired_on,
            'role_id': self.role_id,
            'department': self.department,
            'department_id': self.department_id
        }