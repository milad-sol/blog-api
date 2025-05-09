from fastapi.routing import APIRouter
from fastapi import status, HTTPException, Depends
import database
from hashing import Hash
import schemas
import models
from hashing import Hash
from repository import user
from sqlalchemy.orm import Session

router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(db, request)


@router.get('/{user_id}', response_model=schemas.ShowUser)
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    return user.show(db, user_id)
