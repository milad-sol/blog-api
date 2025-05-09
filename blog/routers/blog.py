from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
import schemas
import models
import database
import oaut2
from repository import blog

router = APIRouter(prefix="/blog", tags=['Blogs'])


@router.get('/', response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(db, request)


@router.delete('/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(blog_id: int, db: Session = Depends(database.get_db)):
    return blog.destroy(db, blog_id)


@router.put('/{blog_id}', status_code=status.HTTP_202_ACCEPTED)
def update(blog_id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(db, blog_id, request)


@router.get('/{blog_id}', response_model=schemas.ShowBlog)
def show(blog_id: int, db: Session = Depends(database.get_db)):
    return blog.show(db, blog_id)
