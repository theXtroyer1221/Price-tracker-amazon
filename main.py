import requests
from bs4 import BeautifulSoup
import smtplib
import time

from art import *

from flask import Flask, render_template

app = Flask("")

@app.route("/")
def helloworld():
  return render_template("index.html", var="PRICE CHECKER")

headers = {"user agent": "Mozilla/5.0 (X11; CrOS aarch64 12239.92.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.136 Safari/537.36"}

class priceApp:
  def __init__(self, app):
    self.app = app

  def runner():
    userwebsite = input("Link of the amazon product: ")
    print("")
    userprice = input("wanted price for check: ")
    print("")
    useremail = input("Email to send to the results: ")
    print("˙" * 50)  
    priceApp.check_price(userwebsite, useremail, userprice)

  def intro():
    tprint("Price checker")
    print("˙" * 50)

  def check_price(url, email, gotprice):
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    #print(soup.prettify())

    title = soup.find(id="productTitle").get_text()

    print(title.strip())

    price = soup.find(id="priceblock_ourprice").get_text()
    priceChangeDot = price.replace(",", ".")
    converted_price = float(priceChangeDot[1:6])
    converted_gotprice = float(gotprice)

    print(f"Price currently: {price}")
    print(f"comparing")

    if(converted_price <= converted_gotprice):
      priceApp.send_mail(email, url)
    else:
      print("Price still high :l per usual")
      print(f"The price you are trying to compare is ${converted_gotprice}")


  def send_mail(email, url):
    try:
      server = smtplib.SMTP("smtp.gmail.com", 587)
      server.ehlo()
      server.starttls()
      server.ehlo()

      server.login("jaddou2005@gmail.com", "wccjxrgoffwxmulu")
    except Exception as e:
      print(e)

    subject = "Price fell down!"
    body = f"Check the link! {url}"

    msg = f"Subject: {subject} {body}"

    server.sendmail("jaddou2005@gmail.com", email, msg)

    server.quit()

    print("Price fell! EMAIL SENT!")

i = 1;
while(i == 1):
  priceApp.intro()
  priceApp.runner()
  i += 1

if (__name__ == "__main__"):
  #app.run(host='0.0.0.0', port=8080)
  pass