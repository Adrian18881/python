######################載入套件######################

import pygame
import sys
import os
from pygame.locals import *

######################定義函式區######################

######################初始化設定######################

os.chdir(sys.path[0])
pygame.init()
clock = pygame.time.Clock()

######################載入圖片######################

img_bg = pygame.image.load("space.png")

######################遊戲視窗設定######################

bg_x = img_bg.get_width() #背景圖片寬度
bg_y = img_bg.get_height() #背景圖片高度
bg_size = (bg_x, bg_y) #背景圖片大小
pygame.display.set_caption("Galaxy Lancer")
screen = pygame.display.set_mode(bg_size)
roll_y = 0

######################玩家設定######################

######################主程式######################

