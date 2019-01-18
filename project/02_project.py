import requests
import json
from bs4 import BeautifulSoup
import csv
import os

my_key = os.getenv("key_token")
name=[]
names=[]
with open('boxoffice.csv', 'r',encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        name=int(item[0])
        names.append(name)


movie_list =[]
movie_dic = dict()
for i in range(len(names)):
    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={my_key}&movieCd={names[i]}'
    req = requests.get(url)
    movies = req.json()
    movie_detale = movies["movieInfoResult"]["movieInfo"] #movie_detale는 딕셔너리

    
    movie_dic['movieCd'] = names[i] #대표네임
    movie_dic['movieNm'] = movie_detale['movieNm'] 
    movie_dic['movieNmEn'] = movie_detale['movieNmEn']
    movie_dic['movieNmOg'] = movie_detale['movieNmOg']
    movie_dic['openDt'] = movie_detale['openDt']
    movie_dic['showTm'] = movie_detale['showTm']
    movie_dic['genreNm'] = movie_detale['genreNm']
    movie_dic['peopleNm'] = movie_detale['peopleNm']
    movie_dic['watchGradeNm'] = movie_detale['watchGradeNm']

    # movie_dic['peopleNm_01'] =movie_detale
    # movie_dic['peopleNm_02'] =movie_detale
    # movie_dic['peopleNm_03'] =movie_detale

    print(movie_list.append(movie_dic))
        
