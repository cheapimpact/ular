import requests, bs4

res = requests.get("https://nostarch.com")
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(noStarchSoup))
print(noStarchSoup.select("#block-block-12"))
