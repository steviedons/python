class Settings():
    """A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        # Ship settings
        self.ship_speed_factor = 1.5
        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 600
        self.bullet_height = 15
        self.bullet_color = 0, 255, 255
        self.bullets_allowed = 10
        self.num_stars = 50
        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # Fleet direction 1 represents right, -1 represents left.
        self.fleet_direction = 1
