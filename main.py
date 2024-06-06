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




@app.post("/regcous/", response_model=schemas.Coursbase) 
def create_cours(cours: schemas.Coursbase, db: Session = Depends(get_db)) -> schemas.Coursbase:
    resp = []
    if int(len(str(cours.CID))) > 5:
        raise HTTPException(status_code=406,detail="CID invalid")
    
    
    db_course = crud.get_course(db, cid=cours.CID)
    if db_course:
        raise HTTPException(status_code=400, detail="CID already registerd")
    return crud.create_course(db=db, course=cours)


@app.get("/delcous/{CID}",response_model=schemas.Coursbase)
def delete_cours(CID:int,cours:schemas.Coursbase ,db:Session=Depends(get_db)):
    db_course = crud.get_course(db,cid=CID)
    if  db_course is None:
        raise HTTPException(status_code=400,detail="CID Dose not exist")
    return crud.delete_cous(db=db, cid=CID)



