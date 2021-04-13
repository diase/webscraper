from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.bbc.com/news"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

articleNames = soup.find_all("h3")

for h in articleNames:
    print(h.get_text())





