from fastapi import Depends, APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
import models.schemas as schemas
from sqlalchemy.orm import Session
from repositories.repositories import UserRepo
from db import get_db
from typing import List
from builtins import bool

router = APIRouter()

@router.post('/',response_model=schemas.User,status_code=201)
async def create_item(item_request: schemas.UserCreate, db: Session = Depends(get_db)):
    """
        Create a new User
    """

    db_user = UserRepo.fetch_by_email(db, email=item_request.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists!")

    return await UserRepo.create(db=db, user=item_request)

@router.get('/',response_model=List[schemas.User])
def get_all_items(db: Session = Depends(get_db)):
    """
    Get all the users
    """
    return UserRepo.fetch_all(db)

@router.get('/{user_id}',response_model=schemas.User)
def get_item(user_id: str,db: Session = Depends(get_db)):
    """
        Get the user by id
    """
    db_user = UserRepo.fetch_by_id(db,user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user

@router.delete('/{user_id}')
async def delete_item(user_id: str,db: Session = Depends(get_db)):
    """
        Delete the user by id
    """
    db_user = UserRepo.fetch_by_id(db,user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await UserRepo.delete(db,user_id)
    return "User deleted successfully!"

@router.put('/{user_id}',response_model=schemas.User)
async def update_item(user_id: str,user_request: schemas.UserUpdate, db: Session = Depends(get_db)):
    """
        Update the user based on the user_id
    """
    db_user = UserRepo.fetch_by_id(db, user_id)
    if db_user:
        update_user_encoded = jsonable_encoder(user_request)
        # todo encode the password
        if 'password' in update_user_encoded:
            db_user.password = update_user_encoded['password']
        if 'is_active' in update_user_encoded:
            db_user.is_active = bool(update_user_encoded['is_active'])
        user_updated =  await UserRepo.update(db=db, user_data=db_user)
        return user_updated
    else:
        raise HTTPException(status_code=400, detail="User not found")