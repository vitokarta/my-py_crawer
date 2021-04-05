import urllib.request as req
url="https://www.ptt.cc/bbs/Gossiping/index.html"

request=req.Request(url, headers={
    "cookie":"over18=1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

import bs4 
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("div", class_="title")
for title in titles:
    if title.a!=None:
        print(title.a.string)


import urllib.request as req
url="https://tw.yahoo.com/"

request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

import bs4 
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("a", class_="Fz(16px) LineClamp(1,20px) Fw(700) Td(n) Td(u):h C(#324fe1) V(h) active_V(v)")
# for title in titles:
#     if title.string!=None:
#         print(title.string)
print(titles)