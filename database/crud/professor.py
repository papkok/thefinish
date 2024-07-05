from sqlalchemy.orm import Session , joinedload 
from database import models
from sqlalchemy.exc import IntegrityError
import Validations.schemas as schemas
#------------------------------------Professor--------------------------------------------------------------------------------------------------------------

def get_prof(db:Session,prof_id:int):
    return db.query(models.Prof).filter(models.Prof.LID == prof_id).first()

async def getthe_prof(db:Session,lid:int):
    try:
       query = db.query(models.Prof).filter(models.Prof.LID==lid).options(joinedload(models.Prof.LcourseID)).first()
       return (True, query , [])
    except BaseException as nig:
        print(nig)
        return (False , {} , [".استاد یافت نشد"])
#_____________________________________________________________________________________________________________________________
def create_profs(db:Session,profs:schemas.Profbase):
    try:
     db_prof = models.Prof(LID=profs.LID,Fname=profs.Fname,Lname=profs.Lname,ID=profs.ID,Department=profs.Department
                          ,Major=profs.Major,Birth=profs.Birth,Borncity=profs.Borncity,Address=profs.Address,
                          PostalCode=profs.PostalCode,Cphone=profs.Cphone,Hphone=profs.Hphone)
     db.add(db_prof)
     db.commit()
     db.refresh(db_prof)
     return db_prof
    except IntegrityError:
        return "یکی از مقادیر واردی قبلا برای کاربر دیگری ثبت شده دوباره تلاش کنید"
#_________________________________________________________________________________________________________________________________
def add_Proffeser_course_relation(db: Session, LID: int, CID: int):
    try: 
        db_cous = db.query(models.Course).filter(models.Course.CID == CID).first()
        db_prof = db.query(models.Prof).filter(models.Prof.LID == LID).first()
        
        
        db_check = db.query(models.prof_course).filter((models.prof_course.c.prof_id == LID) & (models.prof_course.c.Course_id == CID)).first()

        if not db_cous:
            return False, ".درس وجود ندارد"

        if not db_prof:
            return False, ".استاد وجود ندارد"

        if db_check:
            return False, "این درس قبلا ثبت شده است."

        db_prof.LcourseID.append(db_cous)
        db.commit()
        return True, ".درس با موفقیت برای برای استاد ثبت شد"

    except BaseException as e:
        print(e)
        return False, ".درس مورد نظر قبلا ثبت شده است"
#_____________________________________________________________________________________________________________________________________________________
def update_Professor(db: Session, LID: int, prof_update: schemas.Profup):
    Prof = db.query(models.Prof).filter(models.Prof.LID == LID).first()
    if not Prof:
        return None  
    
    update_data = prof_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(Prof, key, value)
    
    db.add(Prof)
    db.commit()
    db.refresh(Prof)
    return Prof
#_____________________________________________________________________________________________________________________________________________________
def delete_profcous(db:Session,LID:int,CID:int):
   try: 
    pf = db.query(models.Prof).filter(models.Prof.LID == LID).first()
    cs = db.query(models.Course).filter(models.Course.CID == CID).first()
    if not pf:
        return False , ".دانشجو وجود ندارد"
    
    if not cs:
        return False , ".استاد وجود ندارد"

    pf.LcourseID.remove(cs)
    db.commit()
    return True , ".استاد مورد نظر حذف شد"
   except BaseException as nigg:
       return False , ".استاد مورد نظر قبلا حذف شده است"
#__________________________________________________________________________________________________________________________________
def delete_prof(db,LID:int):
    prof = db.query(models.Prof).filter(models.Prof.LID == LID).first()
    db.delete(prof)
    db.commit()
    return prof