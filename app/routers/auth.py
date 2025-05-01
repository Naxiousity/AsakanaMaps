from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from ..crud import create_user, get_user_by_email
from ..schemas import UserCreate, UserRead
from ..db import get_session

router = APIRouter()

@router.post("/signup", response_model=UserRead)
def signup(user_in: UserCreate, db: Session = Depends(get_session)):
    if get_user_by_email(db, user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user_in)
