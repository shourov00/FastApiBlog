from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Rabbi'}}


@app.get('/about')
def about():
    return {'data': {'name': 'Abbout Page'}}