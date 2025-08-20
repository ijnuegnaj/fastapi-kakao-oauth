# FastAPI Kakao OAuth Login

카카오 OAuth 2.0 로그인을 **FastAPI** 기반으로 구현한 프로젝트입니다.  
JWT 인증과 DB 저장 기능을 확장할 예정입니다.
현재 Redirect URL mistmatch -> KOE101 오류 발생으로 추후 수정될 예정입니다.

---

## 🚀 프로젝트 개요

- **프레임워크**: FastAPI
- **OAuth 제공자**: Kakao
- **인증 방식**: OAuth 2.0 → JWT 발급 예정
- **DB**: 추후 연동 (사용자 정보 저장)

---

## 📂 프로젝트 구조
├── app/ # 메인 애플리케이션
│ ├── auth.py # Kakao OAuth 인증 로직
│ ├── main.py # FastAPI 엔트리 포인트
│ └── ...
├── .env # 환경변수 (직접 생성 필요)
├── requirements.txt # 의존성 목록
└── .gitignore

---

## ⚙️ 환경 변수 설정

`.env` 파일을 프로젝트 루트에 생성 후 아래와 같이 작성합니다:

```env
KAKAO_CLIENT_ID=카카오_REST_API_KEY
KAKAO_REDIRECT_URI=http://localhost:8000/auth/kakao/callback
SECRET_KEY=jwt_secret_key   # 추후 JWT 발급용

# 가상환경 생성 및 패키지 설치
pip install -r requirements.txt

# 서버 실행
uvicorn app.main:app --reload

