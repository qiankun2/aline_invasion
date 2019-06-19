'''
   创建飞船，并投入到游戏窗口中，最主要是要确定位置。确定位置，需要飞船的坐标和窗口的坐标。

'''
import pygame

class Ship():
    def __init__(self,screen,ai_setting):
        #初始化飞船并初始化起始位置
        self.screen = screen

        #加载飞船图片和获取飞船矩形
        self.image = pygame.image.load('images/ship.bmp')
        #飞船的矩形，实质上就是加载后的飞船图片的矩形
        self.rect =  self.image.get_rect()
        #获取游戏窗口的矩形
        self.screen_rect = screen.get_rect()

        # 飞船移动标志属性
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_bottom = False

        #将每艘飞船都放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #设置飞船矩形的边界和窗口矩形的边界相等，用于控制飞船不出边界
        #self.rect.right = self.screen_rect.right
        #self.rect.left = self.screen_rect.left
        #self.rect.top = self.screen_rect.top

        self.ai_setting = ai_setting
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    # 移动飞船位置
    def mobile(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #if self.rect.right < self.screen_rect.right:
            #self.rect.centerx += 1
            self.centerx += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            #if self.rect.left < self.screen_rect.left:
                #self.rect.centerx -= 1
            self.centerx -= self.ai_setting.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            #if self.rect.top < self.screen_rect.top:
                #self.rect.centery -= 1
            self.centery -= self.ai_setting.ship_speed_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            #if self.rect.bottom < self.screen_rext.bottom:
                #self.rect.centery += 1
            self.centery += self.ai_setting.ship_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

