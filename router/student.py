from fastapi import Depends, APIRouter, HTTPException , Response , status
from sqlalchemy.orm import Session

from Validations import Valdations, schemas

from database.crud import student
from app.Dependency import get_db



app = APIRouter()

@app.get("/getstu/{STID}")
async def get_student(STID:int,res:Response,db:Session = Depends(get_db)):
    valid, data, errors = await student.get_student(db=db,stu=STID)
    res.status_code = status.HTTP_200_OK if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "data": data, "errors": errors}




@app.post("/regstuds/")
def create_student(stud:schemas.Stubase,db:Session=Depends(get_db)):
    validator = Valdations.StudentVald
    validate_data = validator.validate(stud.dict())
    if any(value for value in validate_data.values()):
        raise HTTPException(status_code=400, detail=validate_data)
    
    db_stud = student.getnorm_student(db,stu_id=stud.STID)
    if db_stud:
        raise HTTPException(status_code=400,detail="STID Already registerd")
    return student.create_student(data = stud ,db=db)



@app.patch("/upstu/{STID}", response_model=schemas.stuupdate)
def update_Student(STID: int, stu_update: schemas.stuupdate, db: Session = Depends(get_db)):
    validator = Valdations.StudentVald
    validate_data = validator.validate(stu_update.dict())
    if any(value for value in validate_data.values()):
        raise HTTPException(status_code=400, detail=validate_data)
    
    Stud = student.getnorm_student(db, STID)
    if Stud is None:
        raise HTTPException(status_code=404, detail="Student not found")

    updated_Student = student.update_Student(db=db, STID=STID, Stu_update=stu_update)
    if updated_Student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return updated_Student



@app.put("/add_student_course/{student_id}/{course_id}")
def add_student_to_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    success, message = student.add_student_course_relation(db=db, student_id=student_id, course_id=course_id)
    if success:
        return {"message": message}
    else:
        raise HTTPException(status_code=400, detail=message)
    


@app.put("/add_student_prof/{student_id}/{prof_id}")
def add_student_to_profs(student_id: int , prof_id: int , db:Session = Depends(get_db)):
    success , message = student.add_student_professer_relation(db=db , student_id=student_id , prof_id=prof_id)
    if success:
        return{"message":message}
    else:
        raise HTTPException(status_code=400 , detail=message)



@app.put("/delete_stuprof/{STID}/{LID}")
def Delete_Prof_Stu(STID:int , LID:int , db:Session=Depends(get_db)):
    success , message = student.delete_stuprof(db=db , STID=STID , LID=LID)
    if success:
        return{"message":message}
    else:
        raise HTTPException(status_code=400 , detail=message)



@app.put("/deletestucous/{STID}/{CID}")
def delete_cous_stu(STID:int,CID:int,db:Session=Depends(get_db)):
    success , message = student.delete_stucous(db=db , STID=STID , CID=CID)
    if success:
        return{"message":message}
    else:
        raise HTTPException(status_code=400 , detail=message)



@app.get("/delstud/{stid}")
def Delete_Students(stid:int,db:Session=Depends(get_db)):
    db_stud = student.getnorm_student(db,stu_id=stid)
    if db_stud is None:
        raise HTTPException(status_code=400,detail="STID dose not Exisit.")
    return student.delete_student(db=db,STID=stid)