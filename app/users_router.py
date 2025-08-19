from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.jwt_util import verify_jwt_token
from app.models import User
from app.deps import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
def get_me(token_data: dict = Depends(verify_jwt_token), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == token_data["id"]).first()
    return {"id": user.id, "username": user.username}
