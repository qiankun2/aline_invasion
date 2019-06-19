import sys

import pygame
from pygame.sprite import Group

import game_functions
from setting import Settings
from ship import Ship

#创建游戏函数
def run_game():
    # 初始化背景，让pygame能够正确的工作
    pygame.init()

    #创建一个游戏窗口对象
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    #添加游戏窗口标题
    pygame.display.set_caption("外星人入侵")

    #创建一个飞船实例
    ship = Ship(screen,ai_settings)

    #创建一个Group
    bullets = Group()

    #开始游戏的主循环
    while True:
        game_functions.check_event(ai_settings,screen,ship,bullets)
        ship.mobile()
        bullets.update()
        game_functions.update_screen(ai_settings,screen,ship,bullets)
run_game()