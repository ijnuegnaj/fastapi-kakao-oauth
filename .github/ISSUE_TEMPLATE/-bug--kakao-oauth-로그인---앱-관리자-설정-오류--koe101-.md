---
name: "[Bug] Kakao OAuth 로그인 - 앱 관리자 설정 오류 (KOE101)"
about: 오류 발생 템플릿
title: ''
labels: bug
assignees: ''

---

## 🐞 버그 설명
카카오 로그인 시도 시 `앱 관리자 설정 오류 (KOE101)` 페이지가 노출됨.

## 🚩 재현 방법
1. `/auth/kakao/login` API 호출
2. 카카오 로그인 창에서 승인 후 redirect
3. callback 도착 시 오류 발생

## 📸 에러 화면
- KOE101 오류 화면 캡처 첨부됨

## 💡 예상 원인
- Kakao 개발자 콘솔 Redirect URI 불일치 가능성
- .env의 CLIENT_ID/REDIRECT_URI 설정값 mismatch
- 로컬 환경(127.0.0.1 vs localhost) 차이

## ✅ TODO
- [ ] Kakao 개발자 콘솔 Redirect URI 확인
- [ ] .env CLIENT_ID / REDIRECT_URI 값 검증
- [ ] FastAPI auth.py 내부 redirect_uri 하드코딩 여부 점검
