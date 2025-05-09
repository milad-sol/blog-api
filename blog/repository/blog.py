from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
import models
import schemas


def get_all(db):
    blogs = db.query(models.Blog).all()
    return blogs


def create(db: Session, request: schemas.Blog):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {blog_id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'delete': 'success'}


def update(db: Session, blog_id: int, request: schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {blog_id} not found')
    blog.update(request.model_dump())
    db.commit()
    return {'update': 'success'}


def show(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {blog_id} not found')

    return blog
