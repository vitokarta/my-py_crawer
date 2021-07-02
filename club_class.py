import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path
import subprocess



url=input("請輸入網址")
respond=requests.get(url)
soup=BeautifulSoup(respond.text, "html.parser")

results=soup.find_all("ul", class_="display_none")


all_ep=len(results)
ep=int(input("輸入集數(1~%d) :" %(all_ep)))
result=results[ep-1].select_one("a").get("data-href")
# print(result)


ep=result.replace("https://v.myself-bbs.com/player/play/","")
ep=ep.replace("\r","")
url="https://v.myself-bbs.com/vpx/%s"%(ep)

print(url)

file_name=ep.replace("/","_")
# file_name=file_name[:-1]


r=requests.get(url)
inf=eval(r.text)

server_list=[]
for idx in inf["host"]:
    try:
        now_time = datetime.now()
        requests.get("%svpx/%s" %(idx["host"],ep),timeout=(2.00,2.00))
        server_list.append((datetime.now()-now_time, idx["host"]))
    except Exception as e: pass
server_list=sorted(server_list)



def Download():
    path=Path("")
    path=str(path.resolve())+"\AnimaDownload"
    if not Path(path).is_dir():
        mdcmd= "md %s" %path
        subprocess.Popen(mdcmd, shell=True)

    ffmpeg = "ffmpeg.exe"
    download_url = server_list[0][1]+ep+"/720p.m3u8"  #"https://vpx03.myself-bbs.com/46594/001/720p.m3u8"
    file_path = r"%s\%s.mp4" %(path,file_name)

    cmd = 'ffmpeg -i %s -c copy %s'%(download_url, file_path) #將各部拼接成我們要的格式
    subprocess.Popen(cmd) #執行 Endingggggggg啦5
    print("downloading")

Download()
# https://myself-bbs.com/thread-46558-1-1.html
# https://vpx15.myself-bbs.com/46558/001/720p.m3u8
