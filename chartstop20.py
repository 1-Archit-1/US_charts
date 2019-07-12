import requests,smtplib,ssl,time
from bs4 import BeautifulSoup

def top100():
	url="https://www.billboard.com/charts/hot-100"
	header={"User-Agent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}
	info=requests.get(url, headers=header)
	#print(info.content)
	soup=BeautifulSoup(info.content,'html5lib')
	trendlist=soup.find('div',attrs={'class':'chart-list chart-details__left-rail'})

	#Scraping the content
	arr=[]
	str1=""
	for x in trendlist.findAll('div',attrs={'class':'chart-list-item'}):
		x1=x.find('span',attrs={'class':'chart-list-item__title-text'}).text.strip()
		x2=x.find('div',attrs={'class':'chart-list-item__artist'}).text.strip()
		str1=str1+"Song Title:"+ x1+"\nArtist:"+x2+"\n\n\n"



	#Sending the email	
	context=ssl.create_default_context()
	server=smtplib.SMTP_SSL(host='smtp.gmail.com',port=465)
	server.login(username,password);
	message="Subject: Top 20\n\n"+str1
	server.sendmail(sender_email,receiver_email,message)
	server.quit()

username="Sample@gmail.com"
password="Sample"
sender_email="Sample@gmail.com"
receiver_email="Sample@example.com"

while(1):
	top100()
	time.sleep(7*24*60*60) #sending every week






