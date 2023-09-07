#################################匯入模組#################################
from moviepy.editor import *  #pip install moviepy
import sys
import os
from myfunction.myfunction import *

#################################初始化#################################
os.chdir(sys.path[0])

#################################取得影片資訊#################################
url = "https://www.youtube.com/watch?v=WlfIYn8-1pI"
title, author, length, thumbnail_url, res = get_video_info(url)
print(f"影片解析度:{res}")

#######################下載影片########################
r = input("根據上面的資訊, 請輸入要下載的影片的解析度(720p/480p/360p/240p/144p):")
if download_video(url, r):
    print("Download finished...")
else:
    print("Download failed...")

#######################切割影片########################
video_path = f"{title}.mp4"  # 影片檔案路徑
if os.path.isfile(video_path):  # 判斷影片檔案是否存在
    clip = VideoFileClip(video_path)  # 讀取影片檔案
    print(f"影片長度:{length}秒")
    beg = int(input("請輸入要切割的開始時間(秒):"))
    end = int(input("請輸入要切割的結束時間(秒):"))
    clip = clip.subclip(beg, end)  # 切割影片
    new_file_name = f"{title}-{beg}-{end}.mp4"
    clip.write_videofile(new_file_name)  # 儲存影片
    print(f"影片儲存於{new_file_name}")
else:
    print("找不到影片檔案")