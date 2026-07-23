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

        new_x = self._x + self._vx * self.dt
        new_y = self._y + self._vy * self.dt

        if new_x < self.radius:
            new_x = 2 * self.radius - self._x - self._vx * self.dt
            self._vx = -self._vx

        elif new_x > self.width - 1 - self.radius:
            new_x = 2 * (self.width - 1 - self.radius) - self._x - self._vx * self.dt
            self._vx = -self._vx

        if new_y < self.radius:
            new_y = 2 * self.radius - self._y - self._vy * self.dt
            self._vy = -self._vy

        elif new_y > self.height - 1 - self.radius:
            new_y = 2 * (self.height - 1 - self.radius) - self._y - self._vy * self.dt
            self._vy = -self._vy

        self._x = new_x
        self._y = new_y

        self.current_observation = self.get_observation()

        return self.current_observation

    def render(self):
        pass

    def get_state(self):
        pass

    def episode_done(self) -> bool:
        return self._current_step >= self.max_steps


env = BallEnvironment(width=10, height=10, radius=1, dt=1, max_speed=5, max_steps=1000)
print(env.get_observation())
print(env._x, env._y, env._vx, env._vy)
for _ in range(10):
    env.step()
    print(env.get_observation())