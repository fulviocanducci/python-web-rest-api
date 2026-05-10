from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from databases.session import get_db
from dependencies.auth_dependency import get_current_user
from models.user import User
from repositories.user_repository import UserRepository
from schemas.user_schema import UserCreate, UserDto, UserUpdate
from utils.hash import hash_password

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/", response_model=list[UserDto])
def get_user_all(
    user_id: int = Depends(get_current_user), db: Session = Depends(get_db)
):
    repo = UserRepository(db)
    return repo.get_all()


@router.get("/{id}", response_model=UserDto)
def get_user_by_id(
    id: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)
):
    repo = UserRepository(db)
    user = repo.get_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User não encontrado")
    return user


@router.post("/", response_model=UserDto, status_code=status.HTTP_201_CREATED)
def post_user(
    model: UserCreate,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    repo = UserRepository(db)
    user: User = User(
        name=model.name, email=model.email, password=hash_password(model.password)
    )
    repo.add(user)
    return user


@router.put("/{id}", response_model=UserDto, status_code=status.HTTP_200_OK)
def put_user(
    model: UserUpdate,
    id: int,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    repo = UserRepository(db)
    user: User = repo.get_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    if model.name:
        user.name = model.name
    if model.email:
        user.email = model.email
    if model.password:
        user.password = hash_password(model.password)
    repo.update(user)
    return user


@router.delete("/{id}", response_model=UserDto, status_code=status.HTTP_200_OK)
def delete_user(
    id: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)
):
    repo = UserRepository(db)
    user: User = repo.get_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    repo.delete(user)
    return Response(status_code=204)
