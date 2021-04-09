'''import os

filePath = "C:/Users/User/Desktop/vedio"
file_list=sorted(os.listdir(filePath))
with open("C:/Users/User/Desktop/file_list.txt","w+") as f:
    for file in file_list:
        f.write("file '{}'\n".format(file))
'''

from moviepy.editor import *
import os

# 定義一個數組
L = []

# 訪問 video 資料夾 (假設影片都放在這裡面)
for root, dirs, files in os.walk("C:/Users/User/Desktop/vedio"):
    # 按檔名排序
    files.sort()
    # 遍歷所有檔案
    for file in files:
        # 如果字尾名為 .mp4
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
final_clip.to_videofile("C:/Users/User/Desktop/vedio/target.mp4", fps=24, remove_temp=False)

'''
ffmpeg.exe -f concat -safe 0 -i file_list.txt -c copy output.aac
'''