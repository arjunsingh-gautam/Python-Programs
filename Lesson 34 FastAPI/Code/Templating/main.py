from fastapi import FastAPI,Request
from typing import List
from fastapi.templating import Jinja2Templates

app=FastAPI()
templates=Jinja2Templates(directory="templates")

students:List[dict]=[
    {
        "name":"John Doe",
        "branch":"CSE",
        "subjects":["DBMS","OS","CN"]
    },
    {
        "name":"Anna Smith",
        "branch":"ECE",
        "subjects":["VLSI","OS"]
    },
    {
        "name":"Ben Miller",
        "branch":"EE",
        "subjects":["DBMS","OS","CN"]
    }
    
]

@app.get("/",name="home",include_in_schema=False)
def home(request:Request):
    return templates.TemplateResponse(request,"home.html",{"students":students})

@app.get("/api/students")
def get_details():
    return students
