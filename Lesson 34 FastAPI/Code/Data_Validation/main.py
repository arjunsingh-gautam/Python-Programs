# Module to introduce data-validation in APIs using Pydantic Schemas
from fastapi import FastAPI,status
from .schemas import StudentCreate,StudentResponse

app=FastAPI()

# Dummy Data
students=[
    {"id":1,"name":"John Doe","branch":"CSE"},
    {"id":2,"name":"Annie Smith","branch":"EE"},
    {"id":3,"name":"Bill Gates","branch":"ECE"},
]

# GET APIs

@app.get("/",response_model=list[StudentResponse])
@app.get("/students",response_model=list[StudentResponse])
def get_students():
    return students

# POST APIs
@app.post("/students",response_model=StudentResponse,status_code=status.HTTP_201_CREATED)
def create_students(student:StudentCreate):
    new_id=max(s['id'] for s in students)+1 if students else 1
    new_student={
        "id":new_id,
        "name":student.name,
        "branch":student.branch
    }
    students.append(new_student)
    return new_student
