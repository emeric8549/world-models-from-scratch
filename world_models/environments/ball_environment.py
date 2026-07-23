from base_environment import BaseEnvironment
import numpy as np

class BallEnvironment(BaseEnvironment):
    def __init__(self, width: int, height: int, radius: int = 1, dt: float = 1, max_speed: int = 5, max_steps: int = 1000):
        if width <= 0:
            raise ValueError("Width should be positive")
        if height <= 0:
            raise ValueError("Height should be positive")
        if radius < 0:
            raise ValueError("Radius should be positive")
        if (2 * radius >= width) or (2 * radius >= height):
            raise ValueError("Radius is too big (should be less than width/2 and height/2)")
        if dt <= 0:
            raise ValueError("dt should be positive")
        if max_speed < 0:
            raise ValueError("Max speed should be positive")
        if max_steps <= 0:
            raise ValueError("Max steps should be positive")
        self.width = width
        self.height = height
        self.radius = radius
        self.dt = dt
        self.max_speed = max_speed
        self.max_steps = max_steps

        self._x = width // 2
        self._y = height // 2
        self._vx = 0
        self._vy = 0
        self._current_step = 0

    def reset(self):
        pass

    def get_observation(self):
        pass
    
    def step(self):
        pass

    def render(self):
        pass

    def get_state(self):
        pass

    def episode_done(self):
        pass