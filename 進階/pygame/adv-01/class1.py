######################匯入模組######################
import pygame
import sys
import math

######################初始化######################

pygame.init()  # 啟動 Pygame
PURPLE = (130, 121, 230)
BLACK = (0, 0, 0)
width = 640  # 設定視窗寬度
height = 320  # 設定視窗高度

######################建立視窗######################
screen = pygame.display.set_mode((width, height))  # 設定視窗大小
pygame.display.set_caption("ㄔㄐㄐ")  # 設定視窗標題

backround = pygame.Surface((width, height))
backround.fill(BLACK)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(backround, (0, 0, 225), (200, 100), 30, 0)
            pygame.draw.rect(backround, (0, 255, 0), [230, 130, 60, 40], 5)
            pygame.draw.ellipse(backround, (255, 0, 0), [130, 160, 60, 35], 5)
            pygame.draw.line(backround, (255, 0, 255), (280, 220), (320, 220),
                             3)
            pygame.draw.polygon(backround, (255, 0, 255),
                                [[280, 220], [320, 220], [200, 200]], 0)
            pygame.draw.arc(backround, (255, 10, 0), [100, 100, 100, 50],
                            math.radians(180), math.radians(0), 2)
    print(pygame.mouse.get_pos())

    screen.blit(backround, (0, 0))
    pygame.display.update()