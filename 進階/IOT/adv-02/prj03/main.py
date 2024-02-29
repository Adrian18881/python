import os 
#新增專案

print(os.listdir())
#列出當前工作目錄內容

with open("new_file.txt", "w") as f:
    f.write("Hello, MicroPython")

print(os.listdir())
#創建新文件

os.remove("new_file.txt")

print(os.listdir())
#刪除文件