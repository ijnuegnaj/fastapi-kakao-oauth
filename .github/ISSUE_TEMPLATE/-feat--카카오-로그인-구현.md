---
name: "[Feat] 카카오 로그인 구현"
about: 카카오 OAuth 로그인 기능 구현을 위한 이슈 템플릿
title: ''
labels: feature
assignees: ''

---

## 📝 기능 설명
- 카카오 로그인 구현 (OAuth 인증 플로우)

## 🔧 작업 내용
- [ ] /auth/kakao/login 엔드포인트 구현
- [ ] /auth/kakao/callback 엔드포인트 구현
- [ ] 카카오 액세스 토큰으로 사용자 정보 조회
- [ ] Swagger 문서 반영

## ✅ 완료 조건
- [ ] 로그인 시 카카오 인증 창이 정상적으로 호출된다
- [ ] 로그인 성공 후 user_info JSON이 반환된다

## 📚 참고
- 카카오 개발자 문서: https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api
