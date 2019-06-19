import pygame
from pygame.sprite import Sprite

#创在一个射击类，继承Sprite(精灵类)
class Bullet(Sprite):
    #继承精灵类的构造方法，并创造射击类的特有属性
    def _init_(self,ai_settings,screen,ship):
        super(Bullet, self)._init_()
        self.screen = screen

        #创建一个用于子弹的矩形，起始坐标暂定于 0.0
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)

        #设置子弹真正的起始位置
        self.rect.top = self.ship.top
        self.rect.centerx = self.ship.centerx

        #存储用小数标识的子弹位置
        self.y = float(self.rect.y)

        # 设置子弹的颜色
        self.color = ai_settings.bullet_color

        # 设置射击速度
        self.speed_factor = ai_settings.bullet_speed_factor

     #移动子弹位置(子弹射击)
    def update(self):
        self.y = self.speed_factor
        self.rect.y = self.y

     # 在屏幕上绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
