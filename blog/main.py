from fastapi import FastAPI, Depends, status

from models import Blog, Base
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from schemas import Blog as schemasBlog

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemasBlog, db: Session = Depends(get_db)):
    new_blog = Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs


@app.get('/blog/{blog_id}')
def show(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        

    return blog
