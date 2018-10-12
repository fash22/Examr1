from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from models import Base

from models.user import User

class DocumentDetail(Base):
    __tablename__ = 'document_details'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref=backref('document_details', uselist=False))  # one-to-one with a user

    als = Column(Boolean)
    tor = Column(Boolean)
    f137 = Column(Boolean)