from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
import requests
import os
import jwt
from datetime import datetime, timedelta

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# ✅ Swagger Authorize 버튼 등록용
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/kakao/callback")

KAKAO_CLIENT_ID = os.getenv("KAKAO_CLIENT_ID")
KAKAO_REDIRECT_URI = os.getenv("KAKAO_REDIRECT_URI")
JWT_SECRET = os.getenv("JWT_SECRET", "secret")
JWT_ALGORITHM = "HS256"


# ---------------------------
# 1. 카카오 로그인 URL 리턴
# ---------------------------
@router.get("/kakao/login")
def kakao_login():
    kakao_auth_url = (
        f"https://kauth.kakao.com/oauth/authorize"
        f"?client_id={KAKAO_CLIENT_ID}"
        f"&redirect_uri={KAKAO_REDIRECT_URI}"
        f"&response_type=code"
    )
    return {"auth_url": kakao_auth_url}


# ---------------------------
# 2. 카카오 콜백 (토큰 발급 + JWT 생성)
# ---------------------------
@router.get("/kakao/callback")
def kakao_callback(code: str):
    token_url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": KAKAO_CLIENT_ID,
        "redirect_uri": KAKAO_REDIRECT_URI,
        "code": code,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    token_res = requests.post(token_url, data=data, headers=headers)
    token_json = token_res.json()

    if "access_token" not in token_json:
        raise HTTPException(status_code=400, detail="카카오 토큰 발급 실패")

    access_token = token_json["access_token"]

    # 카카오 유저 정보 요청
    user_res = requests.get(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    user_json = user_res.json()

    # JWT 발급
    payload = {
        "sub": str(user_json["id"]),
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    jwt_token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return {"kakao_user": user_json, "jwt_token": jwt_token}


# ---------------------------
# 3. 보호된 API (JWT 필요)
# ---------------------------
@router.get("/me")
def get_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id = payload.get("sub")
        return {"msg": "인증 성공", "user_id": user_id}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="JWT 만료")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="유효하지 않은 JWT")
