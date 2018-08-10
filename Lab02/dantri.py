from urllib.request import urlopen

# #1. Download web page
# url = "http://dantri.com.vn"
# #1.1. Create connection
# conn = urlopen(url)
# #1.2. Read
# data = conn.read()
# #1.3 Decode
# html_content = data.decode('utf-8')
# print(html_content)

html = urlopen("http://dantri.com.vn").read().decode('utf-8')
#print(html)

#save html to file

url = "http://dantri.com.vn"
# content = urlopen(url)
# html_file = open("dantri.html", "wb")
# html_file.writelines(content)
# html_file.close()

#2. Extract ROI (Region of Interest)
from bs4 import BeautifulSoup
#html, xml, xhtml
soup = BeautifulSoup(html,"html.parser")
#print(soup.prettify())

ul = soup.find("ul", "ul1 ulnew")
#print(ul.prettify())

#3. Extract data
li_list = ul.find_all("li")
data = []

for li in li_list:
    post = {}
    a = li.h4.a
    post["title"] = a.string
    post["url"] = url + a["href"]
    data.append(post)

import pyexcel
pyexcel.save_as(records=data, dest_file_name="Dantri.xlsx") 