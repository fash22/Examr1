
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from models import Base  #Declarative base, performs two task: Defines a table, and maps a python class to it


class PersonPeronalInfoColumns():
    first_name = Column(String(length=20))
    middle_name = Column(String(length=20))
    family_name = Column(String(length=20))


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    user = relationship('User', backref=backref('role')) # one-to-many relationships, many users in one role


    def __repr__(self):
        return '<Role %r>' % self.name


class User(Base, PersonPeronalInfoColumns):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(length=20))
    password_hash = Column(String(length=180))

    role_id = Column(Integer, ForeignKey('roles.id'))

    def __repr__(self):
        return 'User[%s %s %s]' % (self.first_name,self.middle_name, self.family_name)

