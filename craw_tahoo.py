# import requests
# from bs4 import BeautifulSoup

# # 下載 Yahoo 首頁內容
# r = requests.get('https://tw.yahoo.com/')

# # 確認是否下載成功

# soup = BeautifulSoup(r.text, 'html.parser')

# # 以 CSS 的 class 抓出各類頭條新聞
# stories = soup.find_all('a', class_="Fz(16px) LineClamp(1,20px) Fw(700) Td(n) Td(u):h C(#324fe1) V(h) active_V(v)")
# for s in stories:
# # 新聞標題
#     print("標題：" + s.text)
# # 新聞網址
#     print("網址：" + s.get('href'))
# print(root.prettify())


import requests
 
url = "https://vpx.myself-bbs.com/47187/001/720p_000.ts"
myfile = requests.get(url)
 
open('D:/py. 練/vedio.ts', 'wb').write(myfile.content)