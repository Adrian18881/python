#######################匯入模組########################
import os
import sys
from myfunction.myfunction import *

#######################初始化########################
os.chdir(sys.path[0])  # 將工作目錄設置為目前檔案所在的目錄

#######################主程式########################
# 影片連結
u = "https://www.youtube.com/watch?v=WlfIYn8-1pI"
_, _, _, _, res = get_video_info(u)  # 取得影片資訊
print(res)

# 選擇解析度
r = input("根據上面的資訊, 請輸入要下載的影片的解析度(720p/480p/360p/240p/144p):")
# 判斷解析度有沒有在目前的streams裡面
if download_video(u, r):
    print("下載完成")
else:
    print("找不到該解析度的影片")