from fastapi import FastAPI

# create an instance
app = FastAPI()


@app.get("/")
def index():
    return {'Data': 'Hello World'}


@app.get("/about")
def about():
    return {'Data': 'This is a simple API'}
