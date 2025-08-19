# app/models.py
from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=True)   # 일반 회원가입용
    password = Column(String, nullable=True)

    kakao_id = Column(String, unique=True, nullable=True)   # 카카오 로그인용
    email = Column(String, nullable=True)
    nickname = Column(String, nullable=True)
