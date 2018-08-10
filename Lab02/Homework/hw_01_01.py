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
    post = {}
    a1 = li.strong
    a2 = li.h3.a
    a3 = li.h4.a

    post["Number"] = a1.string
    post["Song"] = a2.string
    post["Artist"] = a3.string
    data.append(post)

import pyexcel
pyexcel.save_as(records=data, dest_file_name="iTunes.xlsx") 