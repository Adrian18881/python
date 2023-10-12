######################匯入模組######################
import pygame
import os
import sys
import random
####################定義函式######################


def gophers_update():
    global tick, pos, score, times, gopherr, gopherr_tick
    if tick > max_tick:
        new_pos = random.randint(0, 5)
        pos = pos6[new_pos]
        tick = 0
        times += 1
    else:
        tick += 1

    if gopherr == hoo:
        if gopherr_tick > gopherr_max_tick:
            gopherr = gophers
            gopherr_tick = 0
        else:
            gopherr_tick += 1

    screen.blit(
        gopherr,
        (pos[0] - gophers.get_width() / 2, pos[1] - gophers.get_height() / 2))


def score_update():
    score_sur = score_font.render(str(score), False, RED)
    screen.blit(score_sur, (10, 10))


def check_click(pos, x_min, y_min, x_max, y_max):
    """判斷滑鼠是否點擊在指定的區域內"""
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


def times_update():
    times_sur = times_font.render(str(times), True, RED)
    screen.blit(times_sur, (bg_x - times_sur.get_width() - 10, 10))


def game_over():
    screen.fill(BLACK)
    end_sur = score_font.render(f"Game over +++ Your score is :{score}", False,
                                RED)
    screen.blit(end_sur, (bg_x / 2 - end_sur.get_width() / 2,
                          bg_y / 2 - end_sur.get_height() / 2))


def mouse_update():
    global hammer, hammer_tick

    if hammer == ham1:
        if hammer_tick > hammer_max_tick:
            hammer = ham2
            hammer_tick = 0
        else:
            hammer_tick += 1
    screen.blit(hammer, (mouse_pos[0] - 15, mouse_pos[1] - 15))


####################初始化#####################
os.chdir(sys.path[0])
pygame.init()
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()
tick = 0
max_tick = 20
bg_img = "Gophers_BG_800x600.png"
bg = pygame.image.load(bg_img)

bg_x = bg.get_width()
bg_y = bg.get_height()

######################建立視窗######################

screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("打地鼠")

######################背景物件######################

######################地鼠物件######################

pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450], [610, 450]]

pos = pos6[0]

gophers = pygame.image.load("IMG_0597.jpg")
hoo = pygame.image.load("gophers01.PNG")
gopherr = gophers
gopherr_tick = 0
gopherr_max_tick = 5

######################分數物件######################

score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)
####################撥放音樂######################
mp3_path = "hit.mp3"
pygame.mixer.music.load(mp3_path)  # 音樂載入程式

######################滑鼠物件######################

pygame.mouse.set_visible(False)  #隱藏滑鼠

ham1 = pygame.image.load("Hammer1.png")
ham2 = pygame.image.load("Hammer2.png")
hammer = ham2
hammer_tick = 0
hammer_max_tick = 5

#######################次數物件#####################

times = 0
times_max = 5
typeface = pygame.font.get_default_font()
times_font = pygame.font.Font(typeface, 24)

######################循環偵測######################

while True:
    clock.tick(60)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            hammer = ham1
            pygame.mixer.music.play()  # 播放音樂
            if check_click(mouse_pos, pos[0] - 50, pos[1] - 50, pos[0] + 50,
                           pos[1] + 50):
                tick = max_tick + 1
                score += 1
                gopherr = hoo
    if times >= times_max:
        game_over()
    else:

        screen.blit(bg, (0, 0))
        gophers_update()
        score_update()
        times_update()
        mouse_update()

    pygame.display.update()