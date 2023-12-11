from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blog list'}
    else:
        return {'data': f'{limit} blog list'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
