-- UPDATE classmate
-- SET name='깐따', address='제주'
-- WHERE id=4;

UPDATE classmate
SET name='덕', address='제주'
WHERE id=4 or id=6;
-- 같은 column은 and 연산자이면 안됨.