import pygame

class Ultraman():

    def __init__(self, screen):
        """初始化奥特曼并设置它的位置"""
        self.screen = screen

        # 加载奥特曼并获取它的外接矩形
        self.image = pygame.image.load('images/ultraman.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 将每个奥特曼放在屏幕上面
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
