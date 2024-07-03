from typing import List , Any , Dict

from fastapi import Depends, APIRouter, HTTPException , Response , status, FastAPI
from sqlalchemy.orm import Session

from . import crud, schemas , Valdations

from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class config:
    orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#--------------------------------------Student----------------------------------------
@app.get("/getstu/{STID}")
async def get_student(STID:int,res:Response,db:Session = Depends(get_db)):
    valid, data, errors = await crud.get_student(db=db,stu=STID)
    res.status_code = status.HTTP_200_OK if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "data": data, "errors": errors}




@app.post("/regstuds/",response_model=schemas.Stubase)
def create_student(stud:schemas.Stubase,db:Session=Depends(get_db)):
    validator = Valdations.StudentVald
    validate_data = validator.validate(stud.dict())
    if any(value for value in validate_data.values()):
        raise HTTPException(status_code=400, detail=validate_data)
    
    db_stud = crud.getnorm_student(db,stu_id=stud.STID)
    if db_stud:
        raise HTTPException(status_code=400,detail="STID Already registerd")
    return crud.create_student(data = stud ,db=db)



@app.patch("/upstu/{STID}", response_model=schemas.stuupdate)
def update_Student(STID: int, stu_update: schemas.stuupdate, db: Session = Depends(get_db)):
    validator = Valdations.StudentVald
    validate_data = validator.validate(stu_update.dict())
    if any(value for value in validate_data.values()):
        raise HTTPException(status_code=400, detail=validate_data)
    
    Stud = crud.getnorm_student(db, STID)
    if Stud is None:
        raise HTTPException(status_code=404, detail="Student not found")

    updated_Student = crud.update_Student(db=db, STID=STID, Stu_update=stu_update)
    if updated_Student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return updated_Student


@app.put("/add_student_course/{student_id}/{course_id}")
def add_student_to_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    success, message = crud.add_student_course_relation(db=db, student_id=student_id, course_id=course_id)
    if success:
        return {"message": message}
    else:
        raise HTTPException(status_code=400, detail=message)
    


@app.put("/add_student_prof/{student_id}/{prof_id}")
def add_student_to_profs(student_id: int , prof_id: int , db:Session = Depends(get_db)):
    success , message = crud.add_student_professer_relation(db=db , student_id=student_id , prof_id=prof_id)
    if success:
        return{"message":message}
    else:
        raise HTTPException(status_code=400 , detail=message)



@app.put("/delete_stuprof/{STID}/{LID}")
def Delete_Prof_Stu(STID:int , LID:int , db:Session=Depends(get_db)):
    success , message = crud.delete_stuprof(db=db , STID=STID , LID=LID)
    if success:
        return{"message":message}
    else:
        raise HTTPException(status_code=400 , detail=message)


@app.put("/deletestucous/{STID}/{CID}")
def delete_cous_stu(STID:int,CID:int,db:Session=Depends(get_db)):
    success , message = crud.delete_stucous(db=db , STID=STID , CID=CID)
    if success:
        return{"message":message}
    else:
        raise HTTPException(status_code=400 , detail=message)



@app.get("/delstuds/{stid}")
def Delete_Students(stid:int,db:Session=Depends(get_db)):
    db_stud = crud.getnorm_student(db,stu_id=stid)
    if db_stud is None:
        raise HTTPException(status_code=400,detail="STID dose not Exisit.")
    return crud.delete_student(db=db,STID=stid)
#---------------------------------Professor-------------------------------------------------        
@app.post("/regprof/",response_model=schemas.Profbase)
def create_prof(prof:schemas.Profbase,db:Session=Depends(get_db)):
    db_profs = crud.get_prof(db,prof_id=prof.LID)
    if db_profs:
        raise HTTPException(status_code=400,detail="LID already registerd.")
    return crud.create_profs(db=db,profs=prof)


@app.patch("/upprof/{LID}", response_model=schemas.Profup)
def update_Prof(LID: int, prof_update: schemas.Profup, db: Session = Depends(get_db)):
    prof = crud.get_prof(db=db, prof_id = LID)
    if prof is None:
        raise HTTPException(status_code=404, detail=".استاد یافت نشد")

    updated_prof = crud.update_Professor(db, LID = LID, prof_update=prof_update)
    if updated_prof is None:
        raise HTTPException(status_code=404, detail=".استاد یافت نشد")
    
    return updated_prof




@app.put("/add_porf_course/{LID}/{CID}")
def procous(LID:int,CID:int,db:Session=Depends(get_db)):
    success, message = crud.add_Proffeser_course_relation(db=db, LID = LID, CID=CID)
    if success:
        return {"message": message}
    else:
        raise HTTPException(status_code=400, detail=message)
    


@app.get("/delprofs/{lid}")
def delete_prof(lid:int,db:Session=Depends(get_db)):
    db_profs = crud.get_prof(db,prof_id=lid)
    if db_profs is None:
        raise HTTPException(status_code=400,detail="LID Dose not exist.")
    return crud.delete_prof(db=db,LID=lid)


@app.put("/deleteprfcous/{LID}/{CID}")
def delete_profcous(LID:int,CID:int,db:Session=Depends(get_db)):
    success, message = crud.delete_profcous(db=db, LID = LID, CID=CID)
    if success:
        return {"message": message}
    else:
        raise HTTPException(status_code=400, detail=message)

#-------------------------------------Course------------------------------------------------------
@app.post("/regcous/", response_model=schemas.Coursbase) 
def create_cours(cours: schemas.Coursbase, db: Session = Depends(get_db)) -> schemas.Coursbase:
    resp = []
    if int(len(str(cours.CID))) > 5:
        raise HTTPException(status_code=406,detail="CID invalid")
    
    
    db_course = crud.get_course(db, cid=cours.CID)
    if db_course:
        raise HTTPException(status_code=400, detail="CID already registerd.")
    return crud.create_course(db=db, course=cours)

@app.patch("/UpCourse/{Course_id}", response_model=schemas.Courseup)
def update_Course(Course_id: int, Course_update: schemas.Courseup, db: Session = Depends(get_db)):
    Course = crud.get_course(db=db, cid = Course_id)
    if Course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    updated_Course = crud.update_Course(db, Course_id= Course_id, Course_update=Course_update)
    if updated_Course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return updated_Course


@app.get("/delcous/{CID}")
def delete_cours(CID:int ,db:Session=Depends(get_db)):
    db_course = crud.get_course(db,cid=CID)
    if  db_course is None:
        raise HTTPException(status_code=400,detail="CID Dose not exist.")
    return crud.delete_cous(db=db, cid=CID)



