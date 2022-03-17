from fastapi import FastAPI
from routes.user import user
app =FastAPI()

@app.get('/')
def get_raiz():
    return{"Hola dirigete a /docs"}

@app.post('/')
def post_raiz():
    return{}

app.include_router(user)