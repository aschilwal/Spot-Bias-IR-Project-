from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import re 



def fetch_content(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	league_table = soup.find('div', class_ = 'width100 storytext')
	
	
	# print(league_table)	
	soup1 = BeautifulSoup(str(league_table),'html.parser')
	table = soup1.find_all("p")
	str1 = ''
	for data in table:
		str1=str1+' '+data.getText()

	return str1
	

session = HTMLSession()
url = "https://news.google.com/search?for=republic+world+political+news+india&hl=en-IN&gl=IN&ceid=IN%3Aen"
r = session.get(url)
r.html.render(sleep=1, scrolldown=0)
articles = r.html.find('article')

newslist = []
newsurls = []


'''fetching news links and titles for articles'''

for item in articles:
	try:
		newsitem = item.find('h3', first = True)

		newsarticle = {
			'title' : newsitem.text,
			'link' : newsitem.absolute_links
		}

		curr_link = str(newsitem.absolute_links).lstrip("{'").rstrip("'}")
		newsurls.append(str(newsitem.absolute_links).lstrip("{'").rstrip("'}"))
		newslist.append(newsarticle)

	except:
		pass



print(len(newslist))

# print(newsurls[0])
# print(fetch_content(newsurls[0]))


newscontent = []

for url in newsurls:
	newscontent.append(fetch_content(url))


for con in newscontent:
	print(con)





