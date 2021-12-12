import smtplib
from hacker_news_scraper_no_creds import extract_news

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()


SERVER = 'smtp.gmail.com' # For starters use GMail Server
PORT = 587
FROM = 'lekha.hamsa93@gmail.com'
TO = 'lekha.hamsa93@gmail.com' # Could be list of recipients as well.
PASS = 'Balasuresh12345'


print('Composing Email....')
msg = MIMEMultipart()

msg['Subject'] = 'Top Hacker News Story [Automated Email]' + ' ' + str(now.day) + ' ' + str(now.date())
msg['From'] = FROM
msg['To'] = TO


content = extract_news('https://news.ycombinator.com/')
msg.attach(MIMEText(content, 'html'))

print('Initializing Server')
server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(0) # 1 --> Show me error messages, 0 --> Don't show me error logs
server.ehlo()
server.starttls()

server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print("Email Sent Successfully...")
server.quit()
