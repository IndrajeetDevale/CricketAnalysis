import requests
from bs4 import BeautifulSoup

links = []
mainurl = "https://www.espncricinfo.com/scores/series/8048/season/2020/indian-premier-league?view=results"
html = requests.get(mainurl).text
soup = BeautifulSoup(html, "lxml")
block = soup.findAll('div', {'class':'match-score-block'})
for link in block:
	links.append('https://www.espncricinfo.com/' + link.a.get('href'))
print(links)
