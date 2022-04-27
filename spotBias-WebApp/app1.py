import numpy as np
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import re 
from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier
from flask import Flask, request, jsonify, render_template
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import asyncio
nltk.download('omw-1.4')
import string
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
import sqlite3 as sql

# Create flask app
app = Flask(__name__)
model = pickle.load(open("modell.sav", "rb"))

article=""
user_feedback=""
baisness=""

@app.route("/")
def Home():
    return render_template('index1.html')

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


  

@app.route("/fetch", methods = ["POST"])
def fetch():
	session = HTMLSession()
	url = "https://news.google.com/search?for=republic+world+political+news+india&hl=en-IN&gl=IN&ceid=IN%3Aen"
	try:
		r = session.get(url)
		r.html.render(sleep=1, scrolldown=0)
	
	except RuntimeError as ex:
		articles = r.html.find('article')
		newslist = []
		newsurls = []
		newstitles = []
		count=0
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
				newstitles.append(newsitem.text)
				count=count+1
				if (count==4):
					break
			except:
				pass

		newscontent = []
		for url in newsurls:
			newscontent.append(fetch_content(url))
		#for con in newscontent:
		#	print(con)
		result=len(newstitles)
		print("RESULT COUNT IS :: "+str(result))
		if "There is no current event loop in thread" in str(ex):
			loop = asyncio.new_event_loop()
			asyncio.set_event_loop(loop)
			id2 = newstitles[2]
	return (render_template("index1.html", size = "Number of Fetched NEWS : {}".format(result), id0 = newstitles[0],id1=newstitles[1],
		id2 =newstitles[2],id3=newstitles[3],id_c0 =newscontent[0],id_c1=newscontent[1],id_c2 = newscontent[2],id_c3=newscontent[3]))


def Preprocessing(text):
  #converting into lower case
  text=text.lower()
  #lemmatization
  lemmatizer = WordNetLemmatizer()
  tokens = nltk.word_tokenize(text)
  new_tokens=[] 
  #applying lemmatization
  for token in tokens:
    new_tokens.append(lemmatizer.lemmatize(token))
  #Removing stopwords and Punctuation
  stop = stopwords.words('english') + list(string.punctuation) + ["''","``",".."]
  preprocessed = " ".join(i for i in new_tokens if i not in stop)
  return preprocessed

@app.route("/predict1", methods = ["POST"])
def predict1():
	text = [(x) for x in request.form.values()]
	text = ' '.join(map(str, text))
	vector=TfidfVectorizer(analyzer='word',ngram_range=(1,1))
	preproccessed=Preprocessing(text)
	train= pickle.load(open("Train.pkl", "rb"))
	train=vector.fit_transform(train)
	x_test=vector.transform([preproccessed])
	result = model.predict(x_test)
	result=result[0]
	global article
	global baisness
	article=text
	baisness=result
	return (render_template("index1.html", prediction_text = "News Article is baised towards : {}".format(result)))
	
@app.route("/survey", methods = ["POST"])
def survey():
	user_answer=request.form['party']
	print(article)
	print(baisness)
	print(user_answer)
	try:
		with sql.connect("dataBase.db") as con:
			cur = con.cursor()
			cur.execute("INSERT INTO newsfeedback (News,prediction,userfeedback) VALUES (?,?,?)",(article,baisness,user_answer) )
			con.commit()
			msg = "Record successfully added"
			print(msg)
	except Exception as e:
        	#con.rollback()
        	#msg = "error in insert operation"
        	print(e)
	finally:
        	return (render_template("index1.html", survey_value = "News Article is baised towards : {}".format(user_answer)))
        	con.close()
	

	
	
if __name__ == "__main__":
    app.debug = True
    app.run()

def flush(self):
    pass





