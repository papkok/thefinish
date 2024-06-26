from typing import List , Any , Dict

from fastapi import Depends, APIRouter, HTTPException , Response , status
from sqlalchemy.orm import Session

from . import crud, schemas , Valdations

from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = APIRouter()

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

@app.put("/add_student_course/{student_id}/{course_id}")
def add_student_to_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    success, message = crud.add_student_course_relation(db=db, student_id=student_id, course_id=course_id)
    if success:
        return {"message": message}
    else:
        raise HTTPException(status_code=400, detail=message)

@app.get("/delstuds/{stid}",)
def Delete_Students(stid:int,db:Session=Depends(get_db)):
    db_stud = crud.getnorm_student(db,stu_id=stid)
    if db_stud is None:
        raise HTTPException(status_code=400,detail="STID dose not Exisit.")
    return crud.delete_student(db=db,STID=stid)
#---------------------------------Prof-------------------------------------------------        
@app.post("/regprof/",response_model=schemas.Profbase)
def create_prof(prof:schemas.Profbase,db:Session=Depends(get_db)):
    db_profs = crud.get_prof(db,prof_id=prof.LID)
    if db_profs:
        raise HTTPException(status_code=400,detail="LID already registerd.")
    return crud.create_profs(db=db,profs=prof)

@app.get("/delprofs/{lid}")
def delete_prof(lid:int,db:Session=Depends(get_db)):
    db_profs = crud.get_prof(db,prof_id=lid)
    if db_profs is None:
        raise HTTPException(status_code=400,detail="LID Dose not exist.")
    return crud.delete_prof(db=db,LID=lid)

#-------------------------------------------------------------------------------------------
@app.post("/regcous/", response_model=schemas.Coursbase) 
def create_cours(cours: schemas.Coursbase, db: Session = Depends(get_db)) -> schemas.Coursbase:
    resp = []
    if int(len(str(cours.CID))) > 5:
        raise HTTPException(status_code=406,detail="CID invalid")
    
    
    db_course = crud.get_course(db, cid=cours.CID)
    if db_course:
        raise HTTPException(status_code=400, detail="CID already registerd.")
    return crud.create_course(db=db, course=cours)

@app.get("/delcous/{CID}")
def delete_cours(CID:int ,db:Session=Depends(get_db)):
    db_course = crud.get_course(db,cid=CID)
    if  db_course is None:
        raise HTTPException(status_code=400,detail="CID Dose not exist.")
    return crud.delete_cous(db=db, cid=CID)



