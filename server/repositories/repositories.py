
from sqlalchemy.orm import Session

from models.users import Users as User

class UserRepo:

 async def create(db: Session, user: User):
      db_user = User(
          email=user.email,
          hashed_password=user.hashed_password,
          is_active=user.is_active
        )
      db.add(db_user)
      db.commit()
      db.refresh(db_user)
      return db_user

 def fetch_by_id(db: Session,_id):
     return db.query(User).filter(User.id == _id).first()

 def fetch_by_email(db: Session,email):
     return db.query(User).filter(User.email == email).first()

 def fetch_all(db: Session, skip: int = 0, limit: int = 100):
     return db.query(User).offset(skip).limit(limit).all()

 async def delete(db: Session,user_id):
     db_user= db.query(User).filter_by(id=user_id).first()
     db.delete(db_user)
     db.commit()


 async def update(db: Session,user_data):
    updated_user = db.merge(user_data)
    db.commit()
    return updated_user