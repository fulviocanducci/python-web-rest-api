from datetime import datetime
from venv import create

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from databases.session import get_db
from dependencies.auth_dependency import get_current_user
from models.credit import Credit
from repositories.credit_repository import CreditRepository
from schemas.credit_schema import CreditCreate, CreditDto, CreditUpdate
from utils.utils_models import apply_patch

router = APIRouter(prefix="/credit", tags=["Credit"])


@router.get("/", response_model=list[CreditDto])
def get_credit_all(db: Session = Depends(get_db)):
    repo = CreditRepository(db)
    return repo.get_all()


@router.get("/{id}", response_model=CreditDto)
def get_credit_by_id(
    id: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)
):
    repo = CreditRepository(db)
    credit = repo.get_by_id(id)
    if not credit:
        raise HTTPException(status_code=404, detail="Credit não encontrado")
    return credit


@router.post("/", response_model=CreditDto, status_code=status.HTTP_201_CREATED)
def post_credit(
    model: CreditCreate,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    repo = CreditRepository(db)
    credit: Credit = Credit(name=model.name, created_at=datetime.now())
    repo.add(credit)
    return credit


@router.put("/{id}", response_model=CreditDto, status_code=status.HTTP_200_OK)
def put_credit(
    model: CreditUpdate,
    id: int,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    repo = CreditRepository(db)
    credit: Credit = repo.get_by_id(id)
    if not credit:
        raise HTTPException(status_code=404, detail="Not found")
    apply_patch(credit, model)
    repo.update(credit)
    return credit


@router.delete("/{id}", response_model=CreditDto, status_code=status.HTTP_200_OK)
def delete_credit(
    id: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)
):
    repo = CreditRepository(db)
    credit: Credit = repo.get_by_id(id)
    if not credit:
        raise HTTPException(status_code=404, detail="Not found")
    repo.delete(credit)
    return Response(status_code=204)
