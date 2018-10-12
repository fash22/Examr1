from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from models import Base

from models.user import User

class CourseRecommendation(Base):
    __tablename__ = 'recommendations'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref=backref('recommendations', uselist=False))  # one-to-one with a user

    bsba = Column(Boolean)
    bsentrep = Column(Boolean)
    bsoa = Column(Boolean)
    bsed = Column(Boolean)
    actbsis = Column(Boolean)
    beed = Column(Boolean)