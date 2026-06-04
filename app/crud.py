from .models import Student

def create_student(db, name, email):
    s = Student(name=name, email=email)
    db.add(s)
    db.commit()
    db.refresh(s)
    return s

def get_students(db):
    return db.query(Student).all()
