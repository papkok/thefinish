from sqlalchemy.orm import Session , joinedload , join
from fastapi import Depends, FastAPI, HTTPException
from database import models
from sqlalchemy.exc import IntegrityError
import Validations.schemas as schemas


#------------------------------------Course---------------------------------------------------------------------------------------------------------------

def get_course(db:Session,cid:int):
    return db.query(models.Course).filter(models.Course.CID==cid).first()

#__________________________________________________________________________________________________________________
def create_course(db:Session,course:schemas.Coursbase):
    db_course = models.Course(CID=course.CID,Cname=course.Cname,Department=course.Department,Credit=course.Credit)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

#_________________________________________________________________________________________________________________________
def update_Course(db: Session, Course_id: int, Course_update: schemas.Courseup):
    Course = db.query(models.Course).filter(models.Course.CID == Course_id).first()
    if not Course:
        return None
    
    update_data = Course_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(Course, key, value)
    
    db.add(Course)
    db.commit()
    db.refresh(Course)
    return Course
#______________________________________________________________________________________________________________________________

def delete_cous(db,cid:int):
    cous = db.query(models.Course).filter(models.Course.CID == cid).first()
    db.delete(cous)
    db.commit()
    return '.درس مورد نظر پاک شد'