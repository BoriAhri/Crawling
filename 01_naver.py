import requests
from bs4 import BeautifulSoup

url = "https://naver.com"

req = requests.get(url)

html = req.text

#print(html)

soup = BeautifulSoup(html, "html.parser")

logo = soup.select_one(".menu_area").text

print(logo)