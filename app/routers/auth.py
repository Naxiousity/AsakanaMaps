from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

from ..crud import create_user, get_user_by_email
from ..schemas import UserCreate, UserRead
from ..db import get_session
from ..core.config import settings


router = APIRouter()

@router.post("/signup", response_model=UserRead)
def signup(user_in: UserCreate, db: Session = Depends(get_session)):
    if get_user_by_email(db, user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user_in)

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_session),
):
    user = get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials.",
        )
    token_data = {"sub":user.email}
    access_token= jwt.encode(token_data, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}
