from database import connect

def get_db():
    db = connect.SessionLocal()
    try:
        yield db
    finally:
        db.close()