import requests
import json
from bs4 import BeautifulSoup
import csv
import os

my_key = os.getenv("key_token")
now_time = [20181104, 20181111, 20181118, 20181125, 20181202, 20181209, 20181216, 20181223, 20181230, 20190106]
movieCd_list =[]
movieNm_list=[]
times_list=[]
audiAcc_list=[]
for now_times in now_time:
    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={my_key}&targetDt={now_times}'
    req = requests.get(url)
    movie_rangking = req.json()
    movie_rangkings = movie_rangking['boxOfficeResult']['weeklyBoxOfficeList']
    for i in range(len(movie_rangkings)):
        movie_dict = movie_rangkings[i]
        if movie_dict['movieCd'] not in movieCd_list:
            movieCd_list.append(movie_dict['movieCd'])
            movieNm_list.append(movie_dict['movieNm'])
            audiAcc_list.append(movie_dict['audiAcc'])
            times_list.append(now_times)

        elif movieNm_list[movieCd_list.index(movie_dict['movieCd'])] < movie_dict['movieNm']:
            movieCd_list[movieCd_list.index(movie_dict['movieCd'])] = movie_dict['movieCd']
            movieNm_list[movieCd_list.index(movie_dict['movieCd'])] = movie_dict['movieNm']
            audiAcc_list[movieCd_list.index(movie_dict['movieCd'])] = movie_dict['audiAcc']
            times_list[movieCd_list.index(movie_dict['movieCd'])] = now_times


with open('boxoffice.csv','w',encoding='utf-8') as f:
    for x in range(len(movieCd_list)):
        f.write(f'{movieCd_list[x]}, {movieNm_list[x]},{audiAcc_list[x]},{times_list[x]}\r')

    







