from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from typing import List

app=FastAPI()
templates=Jinja2Templates(directory="templates")

students: List[dict] = [
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

@app.get("/", name="home", include_in_schema=False)
def home(request: Request):
    # TemplateResponse expects the template name first and a context dict
    return templates.TemplateResponse("home.html", {"request": request, "students": students})

@app.get("/api/students")
def get_details():
    return students
