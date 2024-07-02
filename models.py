from sqlalchemy import Boolean, Column, ForeignKey, Integer, String ,Table 
from sqlalchemy.orm import relationship , mapped_column , Mapped
from sqlalchemy.ext.declarative import declarative_base
from .database import Base
Base = declarative_base()


Stu_profs_association = Table(
    'student_proffeser',
    Base.metadata,
    Column('Student_ID', Integer, ForeignKey('Student.STID'),primary_key=True),
    Column('Proffesrt_ID', Integer, ForeignKey('Profs.LID'),primary_key=True,unique=True)
)
stu_cours_asso = Table('student_course',
                       Base.metadata,
                       Column('student_ID',Integer,ForeignKey('Student.STID'),primary_key=True),
                       Column('Course_ID',Integer,ForeignKey('Course.CID'),primary_key=True , unique= True)
)
prof_course = Table('Proffeser_Course',
                    Base.metadata,
                    Column("prof_id",Integer,ForeignKey("Profs.LID"),primary_key=True),
                    Column("Course_id",Integer,ForeignKey("Course.CID"),unique=True)
)


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
    Cphone = Column(String, unique=True)
    Hphone = Column(String, unique=True)
    Department = Column(String)
    Major = Column(String)
    Married = Column(String, default=False)
    ID = Column(String, unique=True)
    
    
    LIDs = relationship("Prof", secondary = Stu_profs_association , backref="Profs")
    ScourseIDs = relationship("Course", secondary = stu_cours_asso ,backref="Course")


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
    LcourseID = relationship("Course",secondary=prof_course,backref="course")
    
    


class Course(Base):
    __tablename__ = "Course"
    CID = Column(Integer, primary_key=True, unique=True)
    Cname = Column(String)
    Department = Column(String)
    Credit = Column(Integer)
    
    
