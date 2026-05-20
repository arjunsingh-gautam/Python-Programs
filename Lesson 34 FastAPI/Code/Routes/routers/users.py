from fastapi import APIRouter,HTTPException,status
from Routes.schemas.user import UserCreate,UserResponse

router=APIRouter(prefix='/users',tags=["Users"])

users:list[dict]=[]

@router.get('/',response_model=list[UserResponse])
def get_users():
    return users

@router.get('/{id}',response_model=UserResponse)
def get_user(id:int):
    for user in users:
        if (user.get('id')==id):
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.post('/',response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def create_user(user:UserCreate):
    for u in users:
        if u.get('id')==user.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User already exist")
    new_user={'id':user.id,'name':user.name}
    users.append(new_user)
    return new_user
    