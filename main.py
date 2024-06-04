from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data' : {'name' : 'Varadha'}}

@app.get('/about')
def about():
    return {'data' : 'Data about page'}