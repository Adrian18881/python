######################匯入模組######################
import pygame
import sys
import math
import os

####################初始化######################

os.chdir(sys.path[0])  #設定程式執行路徑 #絕對路徑

pygame.init()  # 啟動 Pygame

bg_img = "snow.jpg"
bg = pygame.image.load(bg_img)  #下載圖片

bg_x = bg.get_width()  #640 #設定寬
bg_y = bg.get_height()  #400 #設定高

BLACK = (0, 0, 0)

####################定義函式######################


def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max

    if x_match and y_match:
        return True
    else:
        return False


######################建立視窗######################
screen = pygame.display.set_mode((bg_x, bg_y))  # 設定視窗大小
pygame.display.set_caption("start")  # 設定視窗標題

####################撥放音樂######################

mp3_path = "snow-dream.mp3"
pygame.mixer.music.load(mp3_path)  #音樂載入程式
pygame.mixer.music.play()  #撥放音樂
pygame.mixer.music.fadeout(600000)  #設定音樂撥放時間

####################設定文字######################
typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render("Start", True, (255, 255, 255))
tit_w = title.get_width()
tit_h = title.get_height()
####################設定雪花基本參數######################

####################新增fps######################

clock = pygame.time.Clock()

######################循環偵測######################

while True:
    clock.tick(20)  #設定每秒20真執行

################################
paint = False

while True:

    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0, tit_w, tit_h):
                paint = not paint  #點擊時切換畫布狀態

    if paint:
        title = font.render("Start", True, (255, 255, 255))

    else:
        title = font.render("Stop", True, (255, 255, 255))

    screen.blit(bg, (0, 0))
    screen.blit(title, (0, 0))
    pygame.display.update()
