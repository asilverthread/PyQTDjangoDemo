import sqlalchemy
from sqlalchemy import Column, String, Date, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Patient(Base):
    __tablename__ = "pyqt_django_demo_patient"

    id = Column(Integer, primary_key=True)
    patient_first_name = Column(String)
    patient_last_name = Column(String)
    patient_birthdate = Column(Date)

    def __repr__(self):
        return "<User(first='%s', last='%s', birthday='%s')>" % (
            self.patient_first_name,
            self.patient_last_name,
            self.patient_birthdate,
        )