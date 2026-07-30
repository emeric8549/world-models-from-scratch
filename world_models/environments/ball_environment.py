from .base_environment import BaseEnvironment
import numpy as np
import matplotlib.pyplot as plt

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

        self.current_observation = self.reset(True)

    def reset(self, randomize: bool = False) -> np.ndarray:
        if not randomize:
            self._x = self.width // 2
            self._y = self.height // 2
            self._vx = 1
            self._vy = 1

        else:
            self._x = np.random.randint(self.radius, self.width - self.radius)
            self._y = np.random.randint(self.radius, self.height - self.radius)
            self._vx = 0
            self._vy = 0

            max_speed_x = min(self.max_speed, (self.width - 1 - self.radius * 2) / self.dt)
            max_speed_y = min(self.max_speed, (self.height - 1 - self.radius * 2) / self.dt)
            
            while self._vx == 0:
                self._vx = np.random.uniform(-max_speed_x, max_speed_x + 1)
            while self._vy == 0:
                self._vy = np.random.uniform(-max_speed_y, max_speed_y + 1)

        self._current_step = 0
        self.current_observation = self.get_observation()

        return self.current_observation

    def get_observation(self) -> np.ndarray:
        current_observation = np.zeros((self.height, self.width))

        x = round(self._x)
        y = round(self._y)

        for i in range(max(0, y - self.radius), min(self.height, y + self.radius + 1)):
            for j in range(max(0, x - self.radius), min(self.width, x + self.radius + 1)):
                if (i - y) ** 2 + (j - x) ** 2 <= self.radius ** 2:
                    current_observation[i, j] = 1

        return current_observation
    
    def step(self) -> np.ndarray:
        self._current_step += 1

        min_x, max_x = self.radius, self.width - 1 - self.radius
        min_y, max_y = self.radius, self.height - 1 - self.radius
        Lx, Ly = max_x - min_x, max_y - min_y

        px, py = self._x - min_x, self._y - min_y
        if self._vx < 0:
            px = 2 * Lx - px

        if self._vy < 0:
            py = 2 * Ly - py

        new_px = (px + abs(self._vx) * self.dt) % (2 * Lx)
        new_py = (py + abs(self._vy) * self.dt) % (2 * Ly)

        self._x = max_x - (new_px - Lx) if new_px > Lx else new_px + min_x
        self._y = max_y - (new_py - Ly) if new_py > Ly else new_py + min_y

        final_direction_x = 1 if new_px < Lx else -1
        final_direction_y = 1 if new_py < Ly else -1

        self._vx = final_direction_x * abs(self._vx)
        self._vy = final_direction_y* abs(self._vy)

        self.current_observation = self.get_observation()

        return self.current_observation

    def render(self) -> None:
        plt.imshow(self.current_observation, cmap="gray")
        plt.axis("off")
        plt.pause(0.1)
        plt.clf()

    def get_state(self) -> dict:
        return {"x": self._x, "y": self._y, "vx": self._vx, "vy": self._vy}

    def episode_done(self) -> bool:
        return self._current_step >= self.max_steps