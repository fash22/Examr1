from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from models import Base

from models.user import User


class ContactDetail(Base):
    __tablename__ = 'contact_details'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref=backref('contact_details', uselist=False)) # one-to-one with a user

    bac_street = Column(String(25))
    bac_purok = Column(String(25))
    bac_barangay = Column(String(25))

    perm_street = Column(String(25))
    perm_barangay = Column(String(25))
    perm_province = Column(String(25))

    cel_number = Column(String(15))
    tel_number = Column(String(15))
