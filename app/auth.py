import os
import requests #인터넷 요청 보내기
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv #환경변수 파일(.env)에서 값 읽기

load_dotenv()

router = APIRouter(prefix="/auth", tags=["auth"])

KAKAO_CLIENT_ID = os.getenv("KAKAO_CLIENT_ID")
KAKAO_REDIRECT_URI = os.getenv("KAKAO_REDIRECT_URI")

# 카카오 로그인 URL로 리다이렉트
@router.get("/kakao/login")
def kakao_login():
    kakao_auth_url = (
        "https://kauth.kakao.com/oauth/authorize"
        f"?client_id={KAKAO_CLIENT_ID}"
        f"&redirect_uri={KAKAO_REDIRECT_URI}"
        f"&response_type=code"
    )
    return RedirectResponse(url=kakao_auth_url)

# 카카오에서 리다이렉트된 후 콜백 처리
@router.get("/kakao/callback")
def kakao_callback(code: str):
    token_url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": KAKAO_CLIENT_ID,
        "redirect_uri": KAKAO_REDIRECT_URI,
        "code": code,
    }

    res = requests.post(token_url, data=data)
    token_json = res.json()
    access_token = token_json.get("access_token")

    user_info = requests.get(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"}
    ).json()

    return {"user_info": user_info}
