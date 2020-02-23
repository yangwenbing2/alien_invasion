class Settings():
    """存储外信任入侵的所有类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 50

        # 子弹的设置
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60   #这是什么用法？？？
        self.bullets_allowed = 10
