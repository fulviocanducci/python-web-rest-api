from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from databases.session import get_db
from repositories.user_repository import UserRepository
from schemas.login_schema import LoginDto
from utils.auth import create_token
from utils.hash import verify_password

router = APIRouter(prefix="/login", tags=["Login"])


@router.post("/login")
def login(model: LoginDto, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    user = repo.get_by_email(model.email)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    if not verify_password(model.password, user.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = create_token(user.id)
    return {"access_token": token, "token_type": "bearer"}
