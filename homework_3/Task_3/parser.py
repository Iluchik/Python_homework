import requests
from bs4 import BeautifulSoup

st_accept = "text/html"
st_useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36"

headers = {
	"Accept": st_accept,
	"User-Agent": st_useragent
}

req = requests.get("https://mai.ru/", headers)
src = req.text

soup = BeautifulSoup(src, features="html.parser")
title = soup.title.string

print(soup.prettify())