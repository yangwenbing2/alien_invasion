class Settings():
    """存储外信任入侵的所有类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_limit = 2

        # 子弹的设置
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60   #这是什么用法？？？
        self.bullets_allowed = 10

        # 外星人的设置
        self.fleet_drop_speed = 100

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 50
        self.bullet_speed_factor = 30
        self.alien_speed_factor = 10

        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
