from fastapi import FastAPI, Depends, status, HTTPException
from hashing import Hash
import models
from database import engine, get_db
from sqlalchemy.orm import Session
from routers import user, blog
import schemas

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)



@app.post('/', status_code=status.HTTP_201_CREATED, tags=["blogs"])
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete('/blog/{blog_id}', status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
def destroy(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {blog_id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'delete': 'success'}


@app.put('/blog/{blog_id}', status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
def update(blog_id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {blog_id} not found')
    blog.update(request.model_dump())
    db.commit()
    return {'update': 'success'}


# @app.get('/blog', response_model=list[schemas.ShowBlog], tags=["blogs"])
# def get_all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


@app.get('/blog/{blog_id}', response_model=schemas.ShowBlog, tags=["blogs"])
def show(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {blog_id} not found')

    return blog


@app.post('/user', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=["users"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user/{user_id}', response_model=schemas.ShowUser, tags=["users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {user_id} not found')
    return user
