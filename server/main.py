from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from db import get_db, engine
import models.users as users
import models.schemas as schemas
from repositories.repositories import UserRepo
from sqlalchemy.orm import Session
import uvicorn
from typing import List,Optional
from fastapi.encoders import jsonable_encoder

app = FastAPI(
    title="Kantrus",
    description="Kantrus Server",
    version="1.0.0",
)

users.Base.metadata.create_all(bind=engine)

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

@app.post('/users', tags=["Users"],response_model=schemas.User,status_code=201)
async def create_item(item_request: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create an User
    """

    db_user = UserRepo.fetch_by_email(db, email=item_request.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists!")

    return await UserRepo.create(db=db, user=item_request)

@app.get('/users', tags=["Users"],response_model=List[schemas.User])
def get_all_items(db: Session = Depends(get_db)):
    """
    Get all the Users stored in database
    """
    return UserRepo.fetch_all(db)


@app.get('/users/{user_id}', tags=["Users"],response_model=schemas.User)
def get_item(user_id: int,db: Session = Depends(get_db)):
    """
    Get the user from db by id
    """
    db_user = UserRepo.fetch_by_id(db,user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete('/users/{user_id}', tags=["Users"])
async def delete_item(user_id: int,db: Session = Depends(get_db)):
    """
    Delete the user by id
    """
    db_user = UserRepo.fetch_by_id(db,user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await UserRepo.delete(db,user_id)
    return "User deleted successfully!"

@app.put('/users/{item_id}', tags=["Users"],response_model=schemas.User)
async def update_item(user_id: int,user_request: schemas.User, db: Session = Depends(get_db)):
    """
    Update an User stored in the database
    """
    db_user = UserRepo.fetch_by_id(db, user_id)
    if db_user:
        update_user_encoded = jsonable_encoder(user_request)
        db_user.email = update_user_encoded['email']
        # todo encode the password
        db_user.hashed_password = update_user_encoded['password']
        db_user.is_active = update_user_encoded['is_active']
        return await UserRepo.update(db=db, item_data=db_item)
    else:
        raise HTTPException(status_code=400, detail="User not found")

if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)