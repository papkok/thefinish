

from fastapi import Depends, APIRouter, HTTPException 
from sqlalchemy.orm import Session

from Validations import  ValdationsC, schemas
from app.Dependency import get_db
from database.crud import course



app = APIRouter()


#-------------------------------------Course------------------------------------------------------
@app.get("/getcous/{CID}")
def get_course(CID:int,db:Session=Depends(get_db)):
    ourse = course.get_course(db=db , cid=CID)
    return ourse



@app.post("/regcous/", response_model=schemas.Coursbase) 
def create_cours(cours: schemas.Coursbase, db: Session = Depends(get_db)) -> schemas.Coursbase:
    validator = ValdationsC.CousVald
    validate_data = validator.validate(cours.dict())
    if any(value for value in validate_data.values()):
        raise HTTPException(status_code=400, detail=validate_data)
    
    
    if int(len(str(cours.CID))) > 5:
        raise HTTPException(status_code=406,detail="CID invalid")
    
    
    db_course = course.get_course(db, cid=cours.CID)
    if db_course:
        raise HTTPException(status_code=400, detail="CID already registerd.")
    return course.create_course(db=db, course=cours)



@app.patch("/UpCourse/{Course_id}", response_model=schemas.Courseup)
def update_Course(Course_id: int, Course_update: schemas.Courseup, db: Session = Depends(get_db)):
    validator = ValdationsC.CousVald
    validate_data = validator.validate(Course_update.dict())
    if any(value for value in validate_data.values()):
        raise HTTPException(status_code=400, detail=validate_data)
    
    
    Course = course.get_course(db=db, cid = Course_id)
    if Course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    updated_Course = course.update_Course(db, Course_id= Course_id, Course_update=Course_update)
    if updated_Course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return updated_Course




@app.get("/delcous/{CID}")
def delete_cours(CID:int ,db:Session=Depends(get_db)):
    db_course = course.get_course(db,cid=CID)
    if  db_course is None:
        raise HTTPException(status_code=400,detail="CID Dose not exist.")
    return course.delete_cous(db=db, cid=CID)