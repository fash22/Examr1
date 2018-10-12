from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from models import Base  #Declarative base, performs two task: Defines a table, and maps a python class to it


class Question(Base):
    __tablename = 'questions'
    id = Column(Integer, primary_key=True)
    choice_id = Column(Integer, ForeignKey('questions.id'))

class Choice(Base):
    __tablename__ = 'choices'

    value = Column(String(20))
    question = relationship('Question', backref=backref('choice'))