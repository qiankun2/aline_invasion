import sys

import pygame

from ship import Ship
import setting
from bullet import Bullet


def check_event(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
#检测键盘按下事件
def check_keydown_event (event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = True
    elif event.key == pygame.K_SPACE:
        #创建一颗子弹，并加入到bullets中
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

#检测键盘抬起事件
def check_keyup_event(event,ship):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = False

#刷新游戏窗口
def update_screen(ai_settings,screen,ship,bullets):
    #填充背景颜色
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #在游戏窗口内创建飞船
    ship.blitme()
    #刷新屏幕
    pygame.display.flip()

