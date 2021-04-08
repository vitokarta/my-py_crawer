import requests
import os

url = "https://vpx.myself-bbs.com/46125/001_v01/720p_00.ts"
# num = re.findall(r"\d\d*","http://myself-bbs.com/forum.php?mod=viewthread&tid=46125&highlight=%E5%92%92")
# for st in num:
#     if len(st)==5:
#         num=st
#         break
# myfile = requests.get("https://vpx.myself-bbs.com/"+num+"")
myfile = requests.get(url)



if not os.path.exists("vedio"):
        os.mkdir("vedio")  # 建立資料夾
open('C:/python/test/vedio/003.ts', 'wb').write(myfile.content)



# https://vpx.myself-bbs.com/46125/001_v01/720p_000.ts