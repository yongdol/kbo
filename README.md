-
#To-Do
-
1. <del>팀별로 테이블나누기 -> article 테이블로합쳤다.
2. <del>여러페이지의 기사가져오기(지금은 한페이지만 가져온다) => js로 표현된 구조화되지 않은 데이터를 정규표현식(re)을 이용해서 파싱하고, 페이지수가져옴
3. <del>pagination
3. <del>각 구단별 상세 기사페이지 -> 실제기사를 어떻게처리해야하나..실제기사링크로 링크
4. <del>기사 사진을 어떻게해야하나 -> link 저장
5. 스코어보드
6. 날짜별 기사보기
7. 날짜별 스코어보드
8. 경기일정
9. <del>crawling.py 함수화
10. crawling.py -> 크론탭에등록해서 주기적 크롤링하기
12. <del>selenium 드라이버 사용시 브라우저 화면에 안보이게 하기 => PhantomJS 이용
13. nav-var 반응형으로만들기
14. <del>팀별로 기사가져오기(view에서 팀별db의 object를 가져오기)


-
#about
selenium을 이용하면 시간이좀 걸리는듯.
bs를 이용해서 html파싱결과를 파일로 저장해서 원하는 작업을 하는 것이 더 빠를듯. 본문 기사링크도 oid와 aid를 조합하면 만들수 있을것 같다. -> js로표현된 구조화되지 않은 데이터라서 그냥 selenium을 사용

모델을 처음에 잘짜야한다는걸 다시한번느꼈다..