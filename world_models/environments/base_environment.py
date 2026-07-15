from abc import ABC, abstractmethod
from typing import Any

class BaseEnvironment(ABC):
    @abstractmethod
    def reset(self) -> Any:
        """
        Reset the environment to its initial state.
        """
        pass

    @abstractmethod
    def step(self, action: Any) -> Any:
        """
        Take an action in the environment and return the next state.
        """
        pass

    @abstractmethod
    def get_observation(self) -> Any:
        """
        Get the current observation of the environment.
        """
        pass

    @abstractmethod
    def render(self) -> None:
        """
        Render the environment for visualization.
        """
        pass

    @abstractmethod
    def get_state(self) -> Any:
        """
        Get the current state of the environment.
        Debug only. Never used during model training.
        """
        pass

    @abstractmethod
    def episode_done(self) -> bool:
        """
        Check if the environment has reached a terminal state.
        """
        pass