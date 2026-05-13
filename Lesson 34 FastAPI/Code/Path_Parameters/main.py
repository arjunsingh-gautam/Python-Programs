from fastapi import FastAPI

app=FastAPI()

students=[
    {
        "id":1,
        "name":"John Doe",
        "branch":"ECE"
    },
    {
        "id":2,
        "name":"Annie Smith",
        "branch":"EE"
    },
    {
        "id":3,
        "name":"Tom Shelby",
        "branch":"CSE"
    }
    
]

@app.get('/api/students')
def get_students():
    return students

@app.get('/api/student/{id}') # id is path parameter which creates dynamic routes
def get_student(id:int):
    for student in students:
        if student.get("id")==id:
            return student
    else:
        return {"error":'Student Not Found!'}