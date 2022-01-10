# http request
import requests
# bs4 for web scraping
from bs4 import BeautifulSoup
#for email
import smtplib
#for email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# for system datetime manipulation
import datetime

now = datetime.datetime.now()

#email content placeholder
content=''

# extracting hacker news stories 
def extract_news(url):
  print('Extracting hacker news stories...')
  cnt=''
  cnt+=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
  response=requests.get(url)
  content=response.content
  soup= BeautifulSoup(content,'html.parser')
  for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
    cnt += ((str(i+1)+' :: ' + tag.text + "\n" + '<br>') if tag.text!='More' else '')
  return(cnt)  


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>-----<br>')
content += ('<br><br>End of Message')

#lets send the email
 
print('Composing Email ...') 

#update your email Details

# YOUR SMTP SERVER
SERVER = 'smtp.gmail.com'
# gmail's PORT NUMBER 
PORT = 587
# EMAIL IDS
FROM = '****************************************'  #sender's email address
TO = '****************************************'    #receiver's email address
PASS ='*******'                                    #sender's email password

msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO


msg.attach(MIMEText(content,'html'))

print('Initiating Server...')

server = smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM,TO,msg.as_string())

print('Email sent...')

server.quit()
