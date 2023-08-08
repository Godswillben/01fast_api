from enum import Enum
from fastapi import APIRouter, Response, status
from typing import Optional


router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message': 'All blogs provided'}

@router.get('/all',
         summary="Retrieve all blogs", 
         description="This api call simulates fetching all blogs")
def get_all_blogs(page, page_size: Optional[int]=None):
    return {'message':f"All {page_size} blogs on page {page}"}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {'message':f"Blog Type {type}"}

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response:Response):
    if id > 5:
        return {'error':f'Blog {id} not found'}
    return {'message':f"Blog with id {id}"}


