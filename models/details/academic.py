from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from models import Base

from models.user import User

class AcademicRecord(Base):
    __tablename__ = 'academic_records'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref=backref('academic_records', uselist=False))  # one-to-one with a user

    previous_school = Column(String(50))
    year_graduated = Column(String(4))
    gpa = Column(Float)