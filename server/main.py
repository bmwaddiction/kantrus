from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from db import get_db, engine
import models.users as users
import models.schemas as schemas
from repositories.repositories import UserRepo
from sqlalchemy.orm import Session
import uvicorn
from typing import List
from api import apiRouter as ApiRouter

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

app.include_router(ApiRouter.apiRouter)

if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)