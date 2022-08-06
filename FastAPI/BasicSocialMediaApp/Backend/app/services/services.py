from os import path
from sqlalchemy.orm import Session
import app.services.database as _database, app.services.models as _models, app.services.schemas as _schemas


def create_database():
    if not path.exists(path.curdir + "/database.db"):
        return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def register_user(db: Session, user: _schemas.UserCreate):
    fake_hashed_password = user.password + "this_will_be_hashed_soon"
    db_user = _models.User(email=user.email,
                           hashed_password=fake_hashed_password,
                           photo_base64=user.photo_base64)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_by_email(db: Session, email: str):
    return db.query(_models.User).filter(_models.User.email == email).first()


def get_users(db: Session):
    return db.query(_models.User).all()


def delete_user(user_id: int, db: Session):
    user = db.query(_models.User).filter(_models.User.id == user_id).first()
    db.delete(user)
    db.commit()


def create_post(db: Session, user_id: int, post: _schemas.PostCreate):
    post = _models.Post(**post.dict(), owner_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_posts(db: Session, skip: int, limit: int):
    return db.query(_models.Post).offset(skip).limit(limit).all()