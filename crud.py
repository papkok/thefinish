from sqlalchemy.orm import Session , joinedload , join
from fastapi import Depends, FastAPI, HTTPException
from . import schemas , models 



#-----------------------------------------------------------Student---------------------------------------------------------------------------------------------
async def get_student(db:Session,stu:int):
    try:
       query = db.query(models.Student).filter(models.Student.STID==stu).options(joinedload(models.Student.ScourseIDs),joinedload(models.Student.LIDs)).first()
       return (True, query , [])
    except BaseException as nig:
        print(nig)
        return (False , {} , ["student dosent exixst."])
#___________________________________________________________________________________
def getnorm_student(db:Session,stu_id:int):
    return db.query(models.Student).filter(models.Student.STID==stu_id).first()


#______________________________________________________________________________________
def create_student(db:Session,data):
    db_student = models.Student(**data.dict())
    
    
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
#___________________________________________________________________________________________
def add_student_course_relation(db: Session, student_id: int, course_id: int):
   try:
    db_stud = db.query(models.Student).filter(models.Student.STID == student_id).first()
    db_cous = db.query(models.Course).filter(models.Course.CID == course_id).first()
    db_check = db.query(models.stu_cours_asso).filter((models.stu_cours_asso.c.student_ID == student_id) & (models.stu_cours_asso.c.Course_ID == course_id)).first()
    if not db_stud:
        return False, ".دانشجو وجود ندارد"
    
    if not db_cous:
        return False, ".درس وجود ندارد"
    
    if db_check:
        return False , ".درس مورد نظر قبلا انتخاب شده است"
    
    db_stud.ScourseIDs.append(db_cous)
    db.commit()
    return True, ".درس با موفقیت برای دانشجو انتخاب شد"
   except BaseException as Nigg:
       return False , ".درس مورد نظر قبلا ثبت شده است"
#_________________________________________________________________________________________________________________________________       
def add_student_professer_relation(db:Session , student_id:int , prof_id:int):
   try: 
    db_stud = db.query(models.Student).filter(models.Student.STID == student_id).first()
    db_prof = db.query(models.Prof).filter(models.Prof.LID==prof_id).first()
    db_check = db.query(models.Stu_profs_association).filter((models.Stu_profs_association.c.Student_ID == student_id) & (models.Stu_profs_association.c.Proffesrt_ID == prof_id)).first()
    if not db_stud:
        return False , ".دانشجو وجود ندارد"
    
    if not db_prof:
        return False , ".استاد وجود ندارد"
    
    if db_check:
        return False , ".استاد مورد نظر قبلا انتخاب شده است"
    db_stud.LIDs.append(db_prof)
    db.commit()
    return True , ".استاد با موفقیت برای برای دانشجو انتخاب شد"
   except BaseException as Nigg:
       print(Nigg)
       return False , ".استاد مورد نظر قبلا ثبت شده است"
#______________________________________________________________________________________________________________
def update_Student(db: Session, STID: int, Stu_update: schemas.stuupdate):
    Stu = db.query(models.Student).filter(models.Student.STID == STID).first()
    if not Stu:
        return None
    
    update_data = Stu_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(Stu, key, value)
    
    db.add(Stu)
    db.commit()
    db.refresh(Stu)
    return Stu

#_______________________________________________________________________________________________________________
def delete_student(db,STID:int):
    studs = db.query(models.Student).filter(models.Student.STID == STID).first()
    db.delete(studs)
    db.commit()
    return studs


#____________________________________________________________________________________________________________________
def delete_stuprof(db:Session, STID: int , LID: int):
   try: 
    st = db.query(models.Student).filter(models.Student.STID == STID).first()
    pf = db.query(models.Prof).filter(models.Prof.LID == LID).first()
    if not st:
        return False , ".دانشجو وجود ندارد"
    
    if not pf:
        return False , ".استاد وجود ندارد"

    st.LIDs.remove(pf)
    db.commit()
    return True , ".استاد مورد نظر حذف شد"
   except BaseException as Nigg:
       return False , ".استاد مورد نظر اضافه نشده یا قبلا حذف شده است"

#___________________________________________________________________________________________________________
 
def delete_stucous(db:Session,STID:int,CID:int):
   try: 
    st = db.query(models.Student).filter(models.Student.STID == STID).first()
    cs = db.query(models.Course).filter(models.Course.CID == CID).first()
    if not st:
        return False , ".دانشجو وجود ندارد"
    
    if not cs:
        return False , ".درس وجود ندارد"

    st.ScourseIDs.remove(cs)
    db.commit()
    return True , ".درس مورد نظر حذف شد"
   except BaseException as nigg:
       return False , ".درس مورد نظر قبلا حذف شده است"
 
#------------------------------------Professor--------------------------------------------------------------------------------------------------------------

def get_prof(db:Session,prof_id:int):
    return db.query(models.Prof).filter(models.Prof.LID == prof_id).first()


#_____________________________________________________________________________________________________________________________
def create_profs(db:Session,profs:schemas.Profbase):
    db_prof = models.Prof(LID=profs.LID,Fname=profs.Fname,Lname=profs.Lname,ID=profs.ID,Department=profs.Department
                          ,Major=profs.Major,Birth=profs.Birth,Borncity=profs.Borncity,Address=profs.Address,
                          PostalCode=profs.PostalCode,Cphone=profs.Cphone,Hphone=profs.Hphone)
    db.add(db_prof)
    db.commit()
    db.refresh(db_prof)
    return db_prof

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
def update_prof(db, LID: int, prof_id):
    prof = db.query(models.Prof).filter(models.Prof.LID == LID).first()
    for key, value in prof_id.Prof():
        setattr(prof, key, value)
    db.commit()
    db.refresh(prof)
    return prof
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