from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from blog.database import get_db
from blog.models import Blog
from blog.schemas import ShowBlog

router = APIRouter()


@router.get('/blog', response_model=List[ShowBlog], tags=["blogs"])
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs