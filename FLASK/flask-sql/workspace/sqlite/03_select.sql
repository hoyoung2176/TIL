SELECT 영화이름 FROM movies WHERE 상영시간>=150;

SELECT 영화코드,영화이름 FROM movies WHERE 장르='애니메이션';

SELECT 영화이름 FROM movies WHERE 장르='애니메이션' and 제작국가='덴마크';

SELECT 영화이름,누적관객수 FROM movies WHERE 누적관객수>1000000 and 관람등급='청소년관람불가';

SELECT * FROM movies WHERE 개봉연도>=20000101 and 개봉연도<=20091231;
-- LIKE '200%',between 가능

SELECT DISTINCT 장르 FROM movies;
