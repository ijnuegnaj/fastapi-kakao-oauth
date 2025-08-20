# 🚀 FastAPI Kakao OAuth Login  

카카오 OAuth 2.0 로그인을 FastAPI 기반으로 구현한 프로젝트입니다.  
현재는 로그인 및 사용자 정보 조회 기능까지 구현되었으며, JWT 인증과 DB 저장 기능은 확장 예정입니다.  
(현재 기능 개선 중 / 버그 관리 현황은 [Issues](../../issues) 참고)  



## 📌 프로젝트 개요  
- **프레임워크**: FastAPI  
- **OAuth 제공자**: Kakao  
- **인증 방식**: OAuth 2.0 → JWT 발급 예정  
- **DB**: 추후 연동 (사용자 정보 저장 예정)  



## ✅ 구현 현황  
- [x] Kakao OAuth 로그인 (인가 코드 발급, Access Token 요청)  
- [x] 사용자 정보 가져오기  
- [ ] DB 연동 (SQLAlchemy 기반 저장)  
- [ ] JWT 발급 및 인증 흐름  
- [ ] 예외 처리 및 테스트 코드 보강  



## 📂 프로젝트 구조  
```bash
app/                # 메인 애플리케이션
├── main.py         # FastAPI 엔트리 포인트
├── auth.py         # Kakao OAuth 인증 로직
├── users.py        # 사용자 관련 라우터 (DB/JWT 연동 예정)
├── db.py           # SQLAlchemy 세팅 (스켈레톤)
└── security.py     # JWT 발급/검증 로직 (스켈레톤)

.env                # 환경변수 (직접 생성 필요)
requirements.txt    # 의존성 목록
.gitignore


## 🛠️ 설치 및 실행
1. 가상환경 생성 및 패키지 설치
pip install -r requirements.txt

2. 서버 실행
uvicorn app.main:app --reload
