from bs4 import BeautifulSoup as bs

with open("jawn.html") as f:
    soup = bs(f, features="html.parser")

table = soup.find_all(id="Tab1")[0]
tds = table.find_all("td")
print(len(tds))
#print(tds[2], tds[19], tds[19+17])
