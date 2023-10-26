######################匯入模組######################
import pygame
import os
import sys
import random
from pygame.locals import *
####################定義函式######################


def movie_dinosaur():
    global ds_y, jumpState, jumpValue, ds_index

    if jumpState:
        if ds_y >= LIMIT_LOW:
            jumpValue = -jump_height
        if ds_y <= 0:
            jumpValue = jump_height
        ds_y += jumpValue

        # 平滑跳躍
        if jumpValue < 0:
            jumpValue += 3  # 上升速度逐漸減小
        else:
            jumpValue += 3  # 下降速度逐漸增大

        if ds_y >= LIMIT_LOW:
            jumpState = False
            ds_y = LIMIT_LOW  #確保恐龍回到地面

    ds_index = (ds_index - 1) % len(img_dinosaur)
    screen.blit(img_dinosaur[ds_index], (ds_x, ds_y))


def move_cacti():

    global cacti_x

    cacti_x = (cacti_x - cacti_shift) % (bg_x - 100)
    screen.blit(img_cacti, (cacti_x, cacti_y))


def bg_update():
    ###更新背景###
    global bg_roll_x

    bg_roll_x = (bg_roll_x - 10) % bg_x
    screen.blit(img, (bg_roll_x - bg_x, 0))
    screen.blit(img, (bg_roll_x, 0))


####################初始化######################

os.chdir(sys.path[0])
pygame.init
LIMIT_LOW = 140
clock = pygame.time.Clock()

####################載入圖片物件######################

img = pygame.image.load("bg.png")

img_dinosaur = [
    pygame.image.load("小恐龍1.png"),
    pygame.image.load("小恐龍2.png"),
]

img_cacti = pygame.image.load("cacti.png")

bg_x = img.get_width()
bg_y = img.get_height()
bg_roll_x = 0

######################建立視窗######################

screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("Dinosaur")

######################分數物件######################

######################恐龍物件######################

ds_x = 50
ds_y = LIMIT_LOW
ds_index = 0

jumpState = False  #跳 狀態
jumpValue = 0  #跳 值
jump_height = 20  #跳 高度

######################仙人掌物件######################

cacti_x = bg_x - 100  #障礙物x位置
cacti_y = LIMIT_LOW  #障礙物y位置
cacti_shift = 10  #仙人掌移動量

######################循環偵測######################

while True:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE and ds_y <= LIMIT_LOW:  #看恐龍是否在地上
                jumpState = True  #開啟跳躍狀態
                print(event.key, K_SPACE)

    bg_update()
    movie_dinosaur()
    move_cacti()

    pygame.display.update()