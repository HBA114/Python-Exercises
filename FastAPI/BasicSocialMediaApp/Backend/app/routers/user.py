from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import schemas as _schemas, services as _services

router = APIRouter()

@router.post("/users/", tags=["users"], response_model=_schemas.User)
def register_user(user: _schemas.UserCreate,
                  db: Session = Depends(_services.get_db)):
    db_user = _services.get_by_email(db=db, email=user.email)
    if db_user is None:
        return _services.register_user(db=db, user=user)
    else:
        raise HTTPException(status_code=400, detail="This email is in use")


@router.get("/users/", tags=["users"], response_model=List[_schemas.User])
def get_users(db: Session = Depends(_services.get_db)):
    users = _services.get_users(db=db)
    return users


@router.delete("/users/{user_id}/", tags=["users"])
def delete_user(user_id: int, db: Session = Depends(_services.get_db)):
    _services.delete_user(db=db, user_id=user_id)