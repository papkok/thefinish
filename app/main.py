from fastapi import FastAPI
from router import  student , course , professor
from database import models , connect
models.Base.metadata.create_all(bind=connect.engine)


class config:
    orm_mode = True


app = FastAPI()



app.include_router(student.app, tags=["Student"])
app.include_router(professor.app, tags=["Professor"])
app.include_router(course.app, tags=["Course"])