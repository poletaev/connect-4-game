from abc import ABC, abstractmethod
from copy import deepcopy

from base_states import GameState
from base_agent import Agent


class Game(ABC):
    def __init__(self, agents: list[Agent]) -> None:
        super().__init__()
        self.agents = agents
        self.state = None

    @abstractmethod
    def is_game_over(self) -> bool:
        raise NotImplemented()

    @abstractmethod
    def display_state(self) -> None:
        raise NotImplemented()

    @abstractmethod
    def init_state(self) -> GameState:
        raise NotImplemented()

    @abstractmethod
    def update_state(self, action) -> GameState:
        raise NotImplemented()

    def run(self):
        self.display_state()
        while not self.is_game_over():
            for agent in self.agents:
                action = agent.get_action(deepcopy(self.state))
                self.update_state(action)
                self.display_state()
