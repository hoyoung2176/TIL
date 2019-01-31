from flask import Flask, render_template, request, redirect
import os
import datetime
import requests
import csv
from bs4 import BeautifulSoup
from datetime import timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello there!'
# 5월 20일부터 d-day 카운트 출력
@app.route('/dday')
def dday():
    now = datetime.datetime.now()
    fut = datetime.datetime(2019, 5, 20)
    d_day = fut - now
    return f'{d_day.days}일 남았습니다.'
    
# variable routing
@app.route('/hi/<string:name>')
def greeting(name):
    # return f'안녕,{name}'
    # greeting.html 로 위처럼 안녕 누구누구를 출력해주세요.
    return render_template('greeting.html', html_name = name)
    
    
@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number**3}'

# 반복문
@app.route('/movie')
def movie():
    movies = ['극한직업', '정글북', '캡틴마블', '보헤미안랩소디', '완벽한타인']
    return render_template('movie.html', movies=movies)

#fake google
@app.route('/google')
def google():
    return render_template('google.html')
    
#Get방식 핑퐁
@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    print(request.args)
    #나오기는 하나 에러메세지가 나와서
    # name=request.args['name'] 보다 get을 많이 이용함
    name=request.args.get('name')
    msg = request.args.get('msg')
    return render_template('pong.html', text=name, msg=msg)
    

#POST방식 핑퐁
@app.route('/ping_new')
def ping_new():
    return render_template('ping_new.html')

@app.route('/pong_new', methods=['POST'])
def pong_new():
    # a=request.form['name']
    name=request.form.get('name')
    msg = request.form.get('msg')
    return render_template('pong_new.html', text=name, msg=msg)
    
#opgg
@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/opgg_result')
def opgg_result():
    url ='http://www.op.gg/summoner/userName='
    userName = request.args.get('userName')
    response = requests.get(url+userName).text
    soup = BeautifulSoup(response, 'html.parser')
    # 홈페이지 검사를 이용하여 copy->seltion을 가져온다.
    wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    loses =soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
    #wins=wins.text에서 text를 안붙이면 span태그와 같이 모든것이 표시되어 나온다.
    return render_template('opgg_result.html', userName=userName, wins=wins.text, loses=loses.text)
    
# CSV
@app.route('/timeline')
def timeline():
    # 지금까지 기록됭있는 방명록들을 보여주자
    timeline=[]

    with open('timeline.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            
            timeline.append(row)
            

    return render_template('timeline.html', timeline=timeline)
    
@app.route('/timeline/create')
def timeline_create():
    username=request.args.get('username','message')
    message=request.args.get('message')
    
    with open('timeline.csv', 'a', newline='', encoding='utf-8') as f:
        fieldnames = ('username', 'message')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({
            'username': username, 
            'message': message
            
        })
    # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
    
    writer.writerow({
        'username' : username,
        'message' : message
    })
    return redirect('/timeline')
    # return render_template('timeline_create.html', username=username, message=message)


#무조건 맨 아래, 중간에 끼면  이 밑에것이 판단못함.
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
    