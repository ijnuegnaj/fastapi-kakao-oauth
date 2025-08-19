# main.py
import uvicorn
from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app import auth

# ✅ .env 불러오기
from dotenv import load_dotenv
import os

load_dotenv()  # .env 읽기

# 디버깅용 (실제 배포 시에는 빼도 됨)
print("✅ ENV KAKAO_CLIENT_ID:", os.getenv("KAKAO_CLIENT_ID"))
print("✅ ENV KAKAO_REDIRECT_URI:", os.getenv("KAKAO_REDIRECT_URI"))

# DB 생성
Base.metadata.create_all(bind=engine)

# FastAPI 앱
app = FastAPI()

# 라우터 등록
app.include_router(auth.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
