from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, Base, engine
from .crud import create_student, get_students
from .schemas import StudentCreate

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status":"UP"}

@app.post("/students")
def create(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student.name, student.email)

@app.get("/students")
def list_students(db: Session = Depends(get_db)):
    return get_students(db)
