from fastapi import FastAPI,HTTPException,Request,Depends,status
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import Session
from .models import Note,User
from .database import Base,engine,get_db
from .schemas import UserCreate,UserResponse,NoteCreate,NoteResponse
from typing import Annotated

Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get('/',name='home',response_model=list[NoteResponse])
def home(db:Annotated[Session,Depends(get_db)]):
    result=db.execute(select(Note))
    notes=result.scalars().all()
    if not notes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No Notes Found"
        )
    return notes

@app.post('/api/users',response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def create_user(user:UserCreate,db:Annotated[Session,Depends(get_db)]):
    result=db.execute(select(User).where(User.username==user.username))
    existing_user=result.scalars().first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exist"
        )
    result=db.execute(
        select(User).where(User.email==user.email)
    )
    existing_email=result.scalars().first()
    if existing_email:
        HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="email already exists"
        )
    new_user=User(
        username=user.username,
        email=user.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post('/api/notes',response_model=NoteResponse,status_code=status.HTTP_201_CREATED)
def create_note(note:NoteCreate,db:Annotated[Session,Depends(get_db)]):
    result=db.execute(select(User).where(User.id==note.user_id))
    user=result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    new_note=Note(
        title=note.title,
        content=note.content,
        user_id=note.user_id
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@app.get('/posts',response_model=list[NoteResponse])
def get_notes(db:Annotated[Session,Depends(get_db)]):
    result=db.execute(select(Note)).scalars().all()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No Notes Found"
        )
    return result


@app.get('/users',response_model=list[UserResponse])
def get_user(db:Annotated[Session,Depends(get_db)]):
    result=db.execute(select(User)).scalars().all()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No User Found"
        )
    return result