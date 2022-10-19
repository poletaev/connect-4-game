from abc import ABC, abstractmethod
from copy import deepcopy


class Game(ABC):
    def __init__(self, agents: list) -> None:
        super().__init__()
        self.agents = agents

    @abstractmethod
    def is_game_over(self) -> bool:
        raise NotImplemented()

    @abstractmethod
    def display_state(self) -> None:
        raise NotImplemented()

    @abstractmethod
    def init_state(self):
        raise NotImplemented()

    @abstractmethod
    def update_state(self, action):
        raise NotImplemented()

    def run(self):
        self.display_state()
        while not self.is_game_over():
            for agent in self.agents:
                action = agent.get_action(deepcopy(self.state))
                self.update_state(action)
                self.display_state()
