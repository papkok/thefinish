from sqlalchemy.orm import Session

from . import schemas

from . import models

def get_student(db: Session, stu_id: int):
    return db.query(models.Student).filter(models.Student.STID == stu_id).first()




def create_student(db:Session,student:schemas.Stubase):
    db_student = models.Student(STID=student.STID, Fname=student.Fname, Lname=student.Lname,
                                Father=student.Father, Birth=student.Birth,
                                IDS=student.IDS, Borncity=student.Borncity, Address=student.Address,
                                PostalCode=student.PostalCode, Cphone=student.Cphone, Hphone=student.Hphone,
                                Department=student.Department,
                                Major=student.Major, Married=student.Married, ID=student.ID,
                                ScourseIDs=student.ScourseIDs, LIDs=student.LIDs)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student(db, STID: int, sutdent_id):
    stud = db.query(models.Student).filter(models.Student.STID == STID).first()
    for key, value in sutdent_id.Student():
        setattr(stud, key, value)
    db.commit()
    db.refresh(stud)
    return stud


def delete_student(db,STID:int):
    stud = db.query(models.Student).filter(models.Student == STID).first()
    db.delete(stud)
    db.commit()
    return stud

#--------------------------------------------------------------------------------------------

def get_prof(db:Session,prof_id:int):
    return db.query(models.Prof).filter(models.Prof.LID == prof_id).first()



def create_profs(db:Session,profs:schemas.Profbase):
    db_prof = models.Prof(LID=profs.LID,Fname=profs.Fname,Lname=profs.Lname,ID=profs.ID,Department=profs.Department
                          ,Major=profs.Major,Birth=profs.Birth,Borncity=profs.Borncity,Address=profs.Address,
                          PostalCode=profs.PostalCode,Cphone=profs.Cphone,Hphone=profs.Hphone,LcourseID=profs.LcourseID)
    db.add(db_prof)
    db.commit()
    db.refresh(db_prof)
    return db_prof


def update_prof(db, LID: int, prof_id):
    prof = db.query(models.Prof).filter(models.Prof.LID == LID).first()
    for key, value in prof_id.Prof():
        setattr(prof, key, value)
    db.commit()
    db.refresh(prof)
    return prof


def delete_prof(db,LID:int):
    prof = db.query(models.Prof).filter(models.Prof.LID == LID).first()
    db.delete(prof)
    db.commit()
    return prof
#-----------------------------------------------------------------------------------------------------------------------
def get_course(db:Session,cid:int):
    return db.query(models.Course).filter(models.Course.CID==cid).first()


def create_course(db:Session,course:schemas.Coursbase):
    db_course = models.Course(CID=course.CID,Cname=course.Cname,Department=course.Department,Credit=course.Credit)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
def update_cous(db, cid: int, cous_id):
    cous = db.query(models.Course).filter(models.Course.CID == cid).first()
    for key, value in cous_id.Course():
        setattr(cous, key, value)
    db.commit()
    db.refresh(cous)
    return cous


def delete_cous(db,cid:int):
    cous = db.query(models.Course).filter(models.Course.CID == cid).first()
    db.delete(cous)
    db.commit()
    return cous