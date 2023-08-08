from typing import Optional
from fastapi import FastAPI, Response, status
from enum import Enum

app = FastAPI()

@app.get('/')
def index():
    return {"message" : 'Hello World!'}

# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message': 'All blogs provided'}

@app.get('/blog/all', 
         tags=['blog'], 
         summary="Retrieve all blogs", 
         description="This api call simulates fetching all blogs")
def get_all_blogs(page, page_size: Optional[int]=None):
    return {'message':f"All {page_size} blogs on page {page}"}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get("/blog/type/{type}", tags=['blog'])
def get_blog_type(type: BlogType):
    return {'message':f"Blog Type {type}"}

@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response:Response):
    if id > 5:
        return {'error':f'Blog {id} not found'}
    return {'message':f"Blog with id {id}"}

