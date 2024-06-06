from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, schemas

from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#----------------------------------------------------------------------------------        
@app.post("/regprof/",response_model=schemas.Profbase)
def create_prof(prof:schemas.Profbase,db:Session=Depends(get_db)):
    db_profs = crud.get_prof(db,prof_id=prof.LID)
    if db_profs:
        raise HTTPException(status_code=400,detail="LID already registerd.")
    return crud.create_profs(db=db,profs=prof)
#--------------------------------------------------------------------------------
@app.get("/delprofs/{lid}",response_model=schemas.Profbase)
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
#------------------------------------------------------------------------------------------------

@app.get("/delcous/{CID}")
def delete_cours(CID:int ,db:Session=Depends(get_db)):
    db_course = crud.get_course(db,cid=CID)
    if  db_course is None:
        raise HTTPException(status_code=400,detail="CID Dose not exist.")
    return crud.delete_cous(db=db, cid=CID)



