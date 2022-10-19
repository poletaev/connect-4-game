from abc import ABC, abstractmethod

from base_states import GameState, GameAction


class Agent(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_action(self, state: GameState) -> GameAction:
        return None



