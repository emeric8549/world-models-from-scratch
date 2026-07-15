class Transition:
    def __init__(self, observation, action, next_observation, timestamp=None, episode_done=False):
        self.observation = observation
        self.action = action
        self.next_observation = next_observation
        self.timestamp = timestamp
        self.episode_done = episode_done