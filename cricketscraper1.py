import csv
import requests
from bs4 import BeautifulSoup

links = []
mainurl = "https://www.espncricinfo.com/scores/series/8048/season/2020/indian-premier-league?view=results"
html1 = requests.get(mainurl).text
soup1 = BeautifulSoup(html1, "lxml")
block = soup1.findAll('div', {'class':'match-score-block'})
for link in block:
	links.append('https://www.espncricinfo.com/' + link.a.get('href'))

for x in links:
	#url = "https://www.espncricinfo.com/series/8048/scorecard/1237178/royal-challengers-bangalore-vs-sunrisers-hyderabad-eliminator-indian-premier-league-2020-21"
	html = requests.get(x).text
	soup = BeautifulSoup(html, "lxml")
	tables = soup.findAll('table', {'class':'bowler'})
	with open('bowler_data.csv','a',newline='') as csvfile:
		f = csv.writer(csvfile)
		#f.writerow([])
		for table in tables:
			rows = table.findAll('tr')
			for tr in rows:
				data=[]
				cols = tr.findAll('td')
				for td in cols:
					data.append(td.text.strip())
				f.writerow(data)
				print(data)