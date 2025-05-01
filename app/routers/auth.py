from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from ..import crud, schemas
from ..db import get_session

router = APIRouter(prefix="/auth", tags=["auth"])  

@router.post("/signup", response_model=schemas.UserRead)

def signup(user_in: schemas.UserCreate, db: Session = Depends(get_session)):
    if crud.get_user_by_email(db, user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user_in)