from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from models import Base

from models.user import User
from models.user import PersonPeronalInfoColumns

class Father(Base, PersonPeronalInfoColumns):
    __tablename__ = 'father'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref=backref('father', uselist=False))  # one-to-one with a user

class Mother(Base, PersonPeronalInfoColumns):
    __tablename__ = 'mother'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref=backref('mother', uselist=False))  # one-to-one with a user

class Guardian(Base, PersonPeronalInfoColumns):
    __tablename__ = 'guardian'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref=backref('guardian', uselist=False))  # one-to-one with a user