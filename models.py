from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Student(Base):
    __tablename__ = "Student"
    STID = Column(Integer, unique=True, primary_key=True)
    Fname = Column(String)
    Lname = Column(String)
    Father = Column(String)
    Birth = Column(String)
    IDS = Column(String, unique=True)
    Borncity = Column(String)
    Address = Column(String)
    PostalCode = Column(Integer, unique=True)
    Cphone = Column(Integer, unique=True)
    Hphone = Column(Integer, unique=True)
    Department = Column(String)
    Major = Column(String)
    Married = Column(String, default=False)
    ID = Column(Integer, unique=True)
    ScourseIDs = Column(Integer, ForeignKey("Course.CID"))
    LIDs = Column(Integer, ForeignKey("Profs.LID"))
    con1 = relationship("Prof", back_populates="conf")
    con2 = relationship("Course", back_populates="conc")


class Prof(Base):
    __tablename__ = "Profs"
    LID = Column(Integer, primary_key=True, unique=True)
    Fname = Column(String)
    Lname = Column(String)
    ID = Column(Integer, unique=True)
    Department = Column(String)
    Major = Column(String)
    Birth = Column(String)
    Borncity = Column(String)
    Address = Column(String)
    PostalCode = Column(Integer, unique=True)
    Cphone = Column(Integer, unique=True)
    Hphone = Column(Integer, unique=True)
    LcourseID = Column(String, ForeignKey("Course.CID"))
    conf = relationship("Student", back_populates="con1")
    con3 = relationship("Course", back_populates="conc1")


class Course(Base):
    __tablename__ = "Course"
    CID = Column(Integer, primary_key=True, unique=True)
    Cname = Column(String)
    Department = Column(String)
    Credit = Column(Integer)
    conc = relationship("Student", back_populates='con2')
    conc1 = relationship("Prof", back_populates="con3")
