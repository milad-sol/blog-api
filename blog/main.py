from fastapi import FastAPI
import models
from routers import user, blog,authentication
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
