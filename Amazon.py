# WEB SCRAPING
import requests
from bs4 import BeautifulSoup as BS 
# this will make html file parsed and then we can get or navigate thru that html
from smtplib import SMTP
# library used to send an email
#--------------------------------------------------------------------------------------
url = "https://www.amazon.in/Apple-iPhone-13-128GB-Midnight/dp/B09G9HD6PD/ref=sr_1_1_sspa?crid=6KP6QT5OAYTF&keywords=iphone+13&qid=1675345307&sprefix=i%2Caps%2C488&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
#--------------------------------------------------------------------------------------
def extract_price():
    page = requests.get(url,headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})
    soup = BS(page.content,"html.parser")
    price = float(soup.find(class_ = "a-offscreen").text[1:10].replace(",",""))
    return price
#--------------------------------------------------------------------------------------   
SMTP_SERVER = "smtp.gmail.com"
# mail transfer protocol used for mail transfer
PORT = 587
EMAIL_ID = "akmbole2002@gmail.com "
PASSWORD = "hnadhvnkudivjeht"
#--------------------------------------------------------------------------------------
def notify():
    server = SMTP(SMTP_SERVER , PORT)
    server.starttls()# for security we use start tls
    # tls : transport layer security
    server.login(EMAIL_ID,PASSWORD)
    subject = "BUY IMMEDIATELY BRO!"
    body = "Price has fallen , Go buy iPhone 13  Now :  " + url
    message = f"Subject:{subject}\n\n{body}"
    # f used for formatting
    server.sendmail(EMAIL_ID,EMAIL_ID,message)
    server.sendmail(EMAIL_ID,"24arushisharma@gmail.com",message)
    server.quit()
#-------------------------------------------------------------------------------------- 
AFFORDABLE_PRICE = 55000
if extract_price() <= AFFORDABLE_PRICE:
    notify()
#--------------------------------------------------------------------------------------
