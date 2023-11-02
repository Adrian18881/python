######################匯入模組######################
import pygame
import os
import sys
import random
from pygame.locals import *
####################定義函式######################


def movie_dinosaur():
    global ds_y, jumpState, jumpValue, ds_index, ds_center_x, ds_center_y

    if jumpState:
        if ds_y >= LIMIT_LOW:
            jumpValue = -jump_height
        if ds_y <= 0:
            jumpValue = jump_height
        ds_y += jumpValue

        # 平滑跳躍
        if jumpValue < 0:
            jumpValue += 1  # 上升速度逐漸減小
        else:
            jumpValue += 1  # 下降速度逐漸增大

        if ds_y >= LIMIT_LOW:
            jumpState = False
            ds_y = LIMIT_LOW  #確保恐龍回到地面

    ds_index = (ds_index - 1) % len(img_dinosaur)

    ds_center_x = ds_x + img_dinosaur[ds_index].get_width() / 2
    ds_center_y = ds_y + img_dinosaur[ds_index].get_height() / 2
    screen.blit(img_dinosaur[ds_index], (ds_x, ds_y))


def move_cacti():

    global cacti_x, score, cacti_center_x, cacti_center_y

    cacti_x = (cacti_x - cacti_shift) % (bg_x - 100)

    cacti_center_x = cacti_x + img_cacti.get_width() / 2
    cacti_center_y = cacti_y + img_cacti.get_height() / 2
    screen.blit(img_cacti, (cacti_x, cacti_y))

    if cacti_x == 0:
        score += 1


def move_ptera():

    global cacti_x, score, cacti_center_x, cacti_center_y

    cacti_x = (cacti_x - cacti_shift) % (bg_x - 100)

    cacti_center_x = cacti_x + img_cacti.get_width() / 2
    cacti_center_y = cacti_y + img_cacti.get_height() / 2
    screen.blit(img_cacti, (cacti_x, cacti_y))

    if cacti_x == 0:
        score += 1


def bg_update():
    ###更新背景###
    global bg_roll_x

    bg_roll_x = (bg_roll_x - 10) % bg_x
    screen.blit(img, (bg_roll_x - bg_x, 0))
    screen.blit(img, (bg_roll_x, 0))


def score_update():
    score_sur = score_font.render(str(score), False, RED)
    screen.blit(score_sur, (10, 10))


def is_hit(x1, y1, x2, y2, r):
    if ((x1 - x2)**2 + (y1 - y2)**2) < (r * r):
        return True
    else:
        return False


def game_over():
    screen.blit(img_gg, ((bg_x - gg_w) / 2, (bg_y - gg_h) / 2))


####################初始化######################

os.chdir(sys.path[0])
pygame.init()
LIMIT_LOW = 140
PTERA_LIMIT_LOW = 110  #翼龍高度
clock = pygame.time.Clock()
RED = (255, 0, 0)

####################載入圖片物件######################

img = pygame.image.load("bg.png")

img_dinosaur = [
    pygame.image.load("小恐龍1.png"),
    pygame.image.load("小恐龍2.png"),
]

img_cacti = pygame.image.load("cacti.png")
img_gg = pygame.image.load("gameover.png")
img_ptera = [pygame.image.load("翼龍飛飛1.png"), pygame.image.load("翼龍飛飛2.png")]
bg_x = img.get_width()
bg_y = img.get_height()
bg_roll_x = 0

######################建立視窗######################

screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("Dinosaur")

######################分數物件######################

score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)

######################恐龍物件######################

ds_x = 50
ds_y = LIMIT_LOW
ds_index = 0

jumpState = False  #跳 狀態
jumpValue = 0  #跳 值
jump_height = 13  #跳 高度

ds_center_x = ds_x + img_dinosaur[0].get_width() / 2
ds_center_y = ds_y + img_dinosaur[0].get_height() / 2

####################翼龍物件##############################

ptera_x = bg_x - 100  #障礙物x位置
ptera_y = PTERA_LIMIT_LOW  #障礙物y位置
ptera_index = 0
ptera_index = 10
ptera_center_x = ptera_x + img_ptera[0].get_width() / 2
ptera_center_y = ptera_y + img_ptera[0].get_height() / 2
ptera_detect_r = max(img_ptera[0].get_width(),
                     img_ptera[0].get_height()) / 2 - 15

######################仙人掌物件######################

cacti_x = bg_x - 100  #障礙物x位置
cacti_y = LIMIT_LOW  #障礙物y位置
cacti_shift = 10  #仙人掌移動量
cacti_center_x = cacti_x + img_cacti.get_width() / 2
cacti_center_y = cacti_y + img_cacti.get_height() / 2
cacti_detect_r = max(img_cacti.get_width(), img_cacti.get_height()) / 2

##########################遊戲結束物件#######################

gg = False
gg_w = img_gg.get_width()
gg_h = img_gg.get_height()

######################循環偵測######################

while True:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE and ds_y <= LIMIT_LOW:  #看恐龍是否在地上
                jumpState = True  #開啟跳躍狀態
            if event.key == K_RETURN and gg:
                score = 0
                gg = False
                cacti_x = bg_x - 100
                ds_y = LIMIT_LOW
                jumpState = False

    if gg:
        game_over()
    else:

        bg_update()
        movie_dinosaur()
        # move_cacti()
        score_update()

        # gg = is_hit(ds_center_x, ds_center_y, cacti_center_x, cacti_center_y,
        #             cacti_detect_r)

        # pygame.draw.circle(screen, RED,
        #                    (int(cacti_center_x), int(cacti_center_y)),
        #                    cacti_detect_r, 1)

        gg = is_hit(ds_center_x, ds_center_y, ptera_center_x, ptera_center_y,
                    ptera_detect_r)

        pygame.draw.circle(screen, RED,
                           (int(ptera_center_x), int(ptera_center_y)),
                           ptera_detect_r, 1)

    pygame.display.update()