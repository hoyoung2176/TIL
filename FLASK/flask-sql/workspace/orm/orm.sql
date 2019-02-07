-- CREATE
INSERT INTO users (username, email)
VALUES ('junho', 'example@gmail.com')

user = User(username='hoyeong', email='example@gmail.com')

-- READ
SELECT * FROM users;
users = User.query.all()

SELECT * FROM users WHERE username='hoyeong';
users = User.query.filter_by(username='hoyeong').all()

SELECT * FROM users WHERE username='hoyeong' LIMIT 1;
users = User.query.filter_by(username='hoyeong').first()

-- None
miss = User.query.filter_by(username='saffy').first()

-- Get one by id
-- primary key 만 get으로 가져올 수 있다.
SELECT * FROM users WHERE id=1;
user = User.query.get(1)

-- Like
user = User.query.filter(User.email.like('%exam%'')).all()
user = User.query.limit(1).offset(2).all()

-- UPDATE
user = User.query.get(1)
user.username = 'ssafy'
db.session.commit()
user.username

-- DELETE
user = User.query.get(1)
db.session.delete(user)
db.session.commit()
