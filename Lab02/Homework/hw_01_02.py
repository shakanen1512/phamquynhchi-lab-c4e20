from urllib.request import urlopen
url = "https://www.apple.com/itunes/charts/songs/"
html = urlopen(url).read().decode('utf-8')

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"html.parser")
section = soup.find("section", "section chart-grid")
div = section.find("div")
ul = div.find("ul")
li_list = ul.find_all("li")
data = []

for li in li_list:
    a2 = li.h3.a
    a3 = li.h4.a
    song = str.join(" ", (a2.string, a3.string))
    data.append(song)

from youtube_dl import YoutubeDL
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1 
}
dl = YoutubeDL(options)
for i in range(len(data)):
    dl.download([data[i]])