from typing import List , Any , Dict

from fastapi import Depends, APIRouter, HTTPException , Response , status, FastAPI
from sqlalchemy.orm import Session

from Validations import  ValdationsP, schemas
from app.Dependency import get_db
from database.crud import professor





app = APIRouter()

#---------------------------------Professor-------------------------------------------------        
@app.get("/getprof/{LID}")
async def get_student(LID:int,res:Response,db:Session = Depends(get_db)):
    valid, data, errors = await professor.getthe_prof(db=db,lid=LID)
    res.status_code = status.HTTP_200_OK if valid else status.HTTP_400_BAD_REQUEST
    return {"status": valid, "data": data, "errors": errors}



@app.post("/regprof/")
def create_prof(prof:schemas.Profbase,db:Session=Depends(get_db)):
    validator = ValdationsP.ProfVald
    validate_data = validator.validate(prof.dict())
    if any(value for value in validate_data.values()):
        raise HTTPException(status_code=400, detail=validate_data)
    
    db_profs = professor.get_prof(db,prof_id=prof.LID)
    if db_profs:
        raise HTTPException(status_code=400,detail="LID already registerd.")
    return professor.create_profs(db=db,profs=prof)



@app.patch("/upprof/{LID}", response_model=schemas.Profup)
def update_Prof(LID: int, prof_update: schemas.Profup, db: Session = Depends(get_db)):
    validator = ValdationsP.ProfVald
    validate_data = validator.validate(prof_update.dict())
    if any(value for value in validate_data.values()):
        raise HTTPException(status_code=400, detail=validate_data)
    
    prof = professor.get_prof(db=db, prof_id = LID)
    if prof is None:
        raise HTTPException(status_code=404, detail=".استاد یافت نشد")

    updated_prof = professor.update_Professor(db, LID = LID, prof_update=prof_update)
    if updated_prof is None:
        raise HTTPException(status_code=404, detail=".استاد یافت نشد")
    
    return updated_prof


app = APIRouter()

@app.put("/add_porf_course/{LID}/{CID}")
def procous(LID:int,CID:int,db:Session=Depends(get_db)):
    success, message = professor.add_Proffeser_course_relation(db=db, LID = LID, CID=CID)
    if success:
        return {"message": message}
    else:
        raise HTTPException(status_code=400, detail=message)
    



@app.get("/delprofs/{lid}")
def delete_prof(lid:int,db:Session=Depends(get_db)):
    db_profs = professor.get_prof(db,prof_id=lid)
    if db_profs is None:
        raise HTTPException(status_code=400,detail="LID Dose not exist.")
    return professor.delete_prof(db=db,LID=lid)



@app.put("/deleteprfcous/{LID}/{CID}")
def delete_profcous(LID:int,CID:int,db:Session=Depends(get_db)):
    success, message = professor.delete_profcous(db=db, LID = LID, CID=CID)
    if success:
        return {"message": message}
    else:
        raise HTTPException(status_code=400, detail=message)
