class Settings():
    """存储外信任入侵的所有类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60   #这是什么用法？？？
        self.bullets_allowed = 5

        # 外星人的设置
        self.fleet_drop_speed = 10

        # 加快游戏节奏
        self.speedup_scale = 1.1

        # 外星人点数的提高速度
        self.score_scale = 1.5

        # 在任何时候都不应该重置最高得分
        self.high_score = 0


        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 50
        self.bullet_speed_factor = 30
        self.alien_speed_factor = 10

        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1

        # 记分
        self.alien_points = 5

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        # 提高外星人点数
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

