from .database import Base,get_db,engine
from .model import Student
from .schema import StudentCreate,StudentRespone
from fastapi import Depends,FastAPI,HTTPException,Request,status
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Annotated

app=FastAPI()
Base.metadata.create_all(bind=engine)
# CREATE API:POST
@app.post('/api/students',response_model=StudentRespone,status_code=status.HTTP_201_CREATED)
def create_student(student:StudentCreate,db:Annotated[Session,Depends(get_db)]):
    result=db.execute(select(Student).where(Student.name== student.name))
    existing_student=result.scalars().all()
    if existing_student:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Student already exists")
    new_student=Student(name=student.name)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# READ API: GET
@app.get('/api/students',response_model=list[StudentRespone])
def get_students(db:Annotated[Session,Depends(get_db)]):
    result=db.execute(select(Student)).scalars().all()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No student found!")
    return result

# UPDATE API: PUT
@app.put('/api/students',response_model=None,status_code=status.HTTP_202_ACCEPTED)
def update_student(id:int,student_data:StudentCreate,db:Annotated[Session,Depends(get_db)]):
    student=db.get(Student,id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,detail="Student not Found!"
        )
    student.name=student_data.name
    db.commit()
    db.refresh(student)
    return student

# DELETE API: DELETE
@app.delete('/api/students',status_code=status.HTTP_202_ACCEPTED)
def delete_student(id:int,db:Annotated[Session,Depends(get_db)]):
    student=db.get(Student,id)
    if not student:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="No student to delete")
    db.delete(student)
    db.commit()
    return {"message": "Deleted Successfully"}