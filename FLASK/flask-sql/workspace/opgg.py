import requests
from bs4 import BeautifulSoup
url ='http://www.op.gg/summoner/userName='
userName = 'hide on bush'
response = requests.get(url+userName).text
soup = BeautifulSoup(response, 'html.parser')
# 홈페이지 검사를 이용하여 copy->seltion을 가져온다.
wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
loses =soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
print(wins.text)
print(loses.text)