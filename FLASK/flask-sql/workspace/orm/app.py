import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User

# flask 인스턴스 생성
app = Flask(__name__) 

# flask app 에  sqlachemy 관련 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
# db_flask는 변할수 있는 값

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 이면 sqlalchemy 데이터베이스 객체 수정 및 신호 방출 등을 추적합니다. 
#과도한 메모리를 사용하기 때문에 False.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# sqlalchemy 초기화
# db = SQLAlchemy(app)
db.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
# 뷰 함수
# Read
def index():
    # url_for('index') =>>> 라우트를 리턴하고('/') 변수를 넘겨줄수있다.
    # return redirect(url_for('index'))
    # db를 읽고 넘겨줘야함
    users = User.query.all()
    return render_template('index.html', users=users)

# CRUD(크루드)
# Create
@app.route('/users/create')
def create():
    username = request.args.get('username')
    email = request.args.get('email')
    # 컬럼에 변수넣음
    user = User(username=username, email=email) 
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

# Delete
@app.route('/users/delete/<int:id>')
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))
    
# Update
@app.route('/users/edit/<int:id>')
def edit(id):
    user = User.query.get(id)
    return render_template('edit.html', user=user)

@app.route('/users/update/<int:id>')
def update(id):
    user = User.query.get(id)
    username = request.args.get('username')
    email = request.args.get('email')
    
    user.username = username
    user.email = email
    db.session.commit()
    
    return redirect(url_for('index'))








#맨아래 서버를 키기 위함
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)


