# The product I am going to track in this project is a PS5

import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import config

PURCHASE_PRICE = 450
URL = "https://www.amazon.com/PlayStation-5-Console-CFI-1215A01X/dp/B0BCNKKZ91/ref=sr_1_2?crid=3OJOOBDL3OVVH&keywords=ps5&qid=1683460711&sprefix=ps%2Caps%2C296&sr=8-2&th=1"
headers = {
    "User-Agent": config.user_agent,
    "Accept-Language": config.accept_language
}
response = requests.get(url=URL, headers=headers)
contents = response.content
soup = BeautifulSoup(contents, 'lxml')

price = float(soup.find(class_="a-offscreen").get_text().split("$")[1])
print(price)

if price < PURCHASE_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=config.my_email, password=config.password)
        conn.sendmail(from_addr=config.my_email, to_addrs=config.send_email, msg=
                      "Subject:Amazon Price Alert!!!\n\n"
                      f"PlayStation 5 Console CFI-1215A01X is now just {price}"
                      f"\n{URL}"
                      )
    print("email sent.")
