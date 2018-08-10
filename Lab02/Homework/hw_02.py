from urllib.request import urlopen
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
html = urlopen(url).read().decode('utf-8')

# content = urlopen(url)
# html_file = open("vinamilk.html", "wb")
# html_file.writelines(content)
# html_file.close()