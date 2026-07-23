from .transition import Transition
from typing import Iterator

class Trajectory:
    """
    Represents a sequence of transitions describing the evolution of an environment over time.
    """
    def __init__(self):
        self.__transitions = []

    def add_transition(self, transition: Transition) -> None:
        if not isinstance(transition, Transition):
            raise TypeError("Expected a Transition object")
        self.__transitions.append(transition)
    
    def get_window(self, start_index: int, end_index: int) -> list[Transition]:
        if start_index < 0 or end_index > len(self.__transitions) or start_index >= end_index:
            raise ValueError("Invalid window indices")
        return self.__transitions[start_index:end_index]
    
    def __getitem__(self, index: int) -> Transition:
        if index < 0 or index >= len(self.__transitions):
            raise IndexError("Transition index out of range")
        return self.__transitions[index]
    
    def __len__(self) -> int:
        return len(self.__transitions)
    
    def __iter__(self) -> Iterator[Transition]:
        return iter(self.__transitions)