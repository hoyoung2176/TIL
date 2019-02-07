from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#table을 객체로 만듬, SQL에서 CREATE TABLE users와 같다.
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
# nullable 는 비어있을 수 없다.
    email = db.Column(db.String(120), unique=True, nullable=False)

#보기 편하게 만드는 방법
    def __repr__(self):
        return f"<User '{self.username}'>"