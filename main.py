
import requests
from bs4 import BeautifulSoup

from smtplib import *


headers={
    "User-Agent":"your user-agent",
    "Accept-Language":"your accept-language"
}

link="https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ?th=1"
data=requests.get(link,headers=headers)
amazon_webpage=data.text

soup= BeautifulSoup(amazon_webpage,"html.parser")
price=float(soup.find(class_="a-price-whole").getText().replace('.',''))
title=soup.find(id="productTitle").getText().strip().encode("ascii",'ignore').decode('ascii')
my_email="youremail@gmail.com"
password="yourpassword"


if price<100:
    with SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs="toaddress", msg=f"Subject: Amazon Price Alert!\n\n"
                                                                                       f"{title} is now:  ${price}\n"
                                                                                       f"{link}")


