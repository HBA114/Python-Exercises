from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import schemas as _schemas, services as _services

router = APIRouter()



@router.post("users/{user_id}/posts/",
          tags=["posts"],
          response_model=_schemas.Post)
def create_post(user_id: int,
                post: _schemas.PostCreate,
                db: Session = Depends(_services.get_db)):
    return _services.create_post(db=db, user_id=user_id, post=post)


@router.get("/posts/", tags=["posts"], response_model=List[_schemas.Post])
def get_posts(skip: int = 0,
              limit: int = 10,
              db: Session = Depends(_services.get_db)):
    return _services.get_posts(db=db, skip=skip, limit=limit)
