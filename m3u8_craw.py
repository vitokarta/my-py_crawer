import datetime 
import requests
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import re

def get_m3u8(url):
    nums = re.findall(r"\d+\d*",url)
    for st in nums:
        if len(st)==5:
            num=st
            break

    url="https://vpx.myself-bbs.com/"+str(num)+"/100/720p.m3u8"
    base_url="https://vpx.myself-bbs.com/"+str(num)+"/100/"


    try:
        myfile=requests.get(url)
    except Exception as e:
        print("異常請求：%s"%e.args)
        return
    with open('D:/py. 練/001.m3u8', 'wb') as f:
        f.write(myfile.content)
    return base_url

def get_ts_urls():
    urls= []
    with open("001.m3u8","r") as file:
        lines = file.readlines()
        for line in lines:
            if(line.endswith(".ts\n")):
                urls.append(base_url+line.strip("\n"))
    return urls

def downloads(ts_urls, download_path):

    for i in range (len(ts_urls)):
        ts_url= ts_urls[i]
        file_name = ts_url.split("/")[-1]
        print("start download %s" %file_name)
        if not os.path.exists("vedio"):
            os.mkdir("vedio")  # 建立資料夾
        try:
            response = requests.get(ts_url)
            
        except Exception as e:
            print("異常請求：%s"%e.args)
            return
            
        ts_path = download_path+"/{0}.ts".format(i)
        with open(ts_path,"wb+") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

def conbine():
    # 定義一個數組
    L = []

    # 訪問 video 資料夾 (假設影片都放在這裡面)
    for root, dirs, files in os.walk("D:/py. 練/vedio"):
    # 按檔名排序
        files.sort()
    # 遍歷所有檔案
        for file in files:
        # 如果字尾名為 .ts
            if os.path.splitext(file)[1] == '.ts':
            # 拼接成完整路徑
                filePath = os.path.join(root, file)
            # 載入影片
                video = VideoFileClip(filePath)
            # 新增到陣列
                L.append(video)
                print(video)

    # 拼接影片
    final_clip = concatenate_videoclips(L)

    # 生成目標影片檔案
    final_clip.to_videofile("D:/py. 練/target.mp4", fps=24, remove_temp=False)

# url=input("請輸入myself動漫網址:")

# base_url=get_m3u8("https://myself-bbs.com/forum.php?mod=viewthread&tid=47275&highlight=BL")
base_url="https://vpx.myself-bbs.com/"+"47275"+"/100/"
urls=get_ts_urls()
downloads(urls,"D:/py. 練/vedio") #待抓
conbine()



#m3u8 https://vpx01.myself-bbs.com/46143/001/720p.m3u8
#單集 https://vpx01.myself-bbs.com/46143/001/720p_000.ts 